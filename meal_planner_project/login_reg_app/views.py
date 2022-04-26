from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

def login(request):
    if request.method == 'GET':
        return render(request, 'login_reg_app/login.html')
    if request.method == 'POST':
        login_errors = User.objects.login_validator(request.POST)
        this_user = User.objects.filter(email = request.POST["email"])
        #validate login
        if len(login_errors) or len(this_user) <= 0:
            for k, v in login_errors.items():
                messages.info(request, v)
            return redirect('/')
        else:
            request.session['user_id'] = this_user.first().id
            return redirect('/dashboard')


        # login_errors = User.objects.login_validator(request.POST)
        # user = User.objects.filter(email=request.POST['email'])
        # if len(login_errors) or len(user) <= 0:
        #     for key, value in login_errors.items():
        #         messages.info(request, value)
        #     return redirect('/')
        # if user:
        #     logged_user = user[0]
        #     if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
        #         request.session['user_id'] = logged_user.id
        #         return redirect('/dashboard')
        #     else:
        #         messages.error(request, "Invalid email address or password!")
        # return redirect('/dashboard')

def registration(request):
    if request.method == 'GET':
        return render(request, 'login_reg_app/registration.html')
    if request.method == 'POST':
        errors = User.objects.registration_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/registration')
        else:
            pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            print(pw_hash)
            user = User.objects.create(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                password=pw_hash
            )
            request.session['user_id'] = user.id
            return redirect('/dashboard')

def dashboard(request):
    if not 'user_id' in request.session:
        return redirect('/')
    else:
        context = {
            'user': User.objects.get(id=request.session['user_id'])
        }
        return render(request, 'login_reg_app/dashboard.html', context)

def logout(request):
    request.session.clear()
    # messages.error(request, "You have successfully logged out.")
    return redirect('/')
