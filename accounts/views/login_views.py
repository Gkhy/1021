from django.shortcuts import render, redirect
from ..forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.




def login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
        return redirect('reviews:index')
    
    else:
        login_form = AuthenticationForm
    context = {
        'login_form' : login_form
    }
    
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('reviews:index')