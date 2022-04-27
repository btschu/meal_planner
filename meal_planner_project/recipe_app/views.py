from django.shortcuts import render, redirect
from login_reg_app.models import User

def dashboard(request):
    if not 'user_id' in request.session:
        return redirect('/')
    else:
        context = {
            'user': User.objects.get(id=request.session['user_id'])
        }
        return render(request, 'recipe_app/dashboard.html', context)