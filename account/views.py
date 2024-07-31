from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .forms import RegisterUserForm


def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Registration Success!!')
            return redirect('index')
    else:
        form = RegisterUserForm()
    return render(request, 'registration/signup.html', {'form': form})


def LoginPage(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        new_user = authenticate(username=username, password=password)
        if new_user is not None:
            login(request, new_user)
            messages.success(request, "Good job !!!")
            return redirect('index')
        else:
            messages.success(request, "Error !!!")

    return render(request, 'registration/login.html', {})


def LogoutPage(request):
    logout(request)
    messages.success(request, "Good job !!!")
    return redirect('index')


def Users(request):
    users = User.objects.filter(is_superuser=False)
    return render(request, 'registration/users.html', {'users': users})


def user(request):
    return render(request, 'registration/user_profile.html')

