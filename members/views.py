from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.http import HttpResponseRedirect




def about(request):
    return render(request, 'members/about.html')

def watchlist(request):
    return render(request, 'members/watchlist.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return render(request, 'movies/index.html')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, "Username/Password invalid")
            return render(request, 'members/login.html')
    else:
        return render(request, 'members/login.html')


def logout_user(request):
    logout(request)
    # Redirect to a success page.
    return render(request, 'movies/index.html')


def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration Successful!")
            return render(request, 'home_view')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form
    }
    return render(request, 'members/register.html', context)