from django.shortcuts import render

def login(request):
    return render(request, 'login_reg_app/login.html')

def registration(request):
    return render(request, 'login_reg_app/registration.html')
