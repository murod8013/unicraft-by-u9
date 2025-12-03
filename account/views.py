from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .form import RegistrationForm,LoginForm
from education.edu_models.student import Student


# from .education.edu_models import Student


# Create your views here.


def create_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            if user:
                Student.objects.create(user=user)
            try:
                login(request, user)
            except Exception as e:
                return redirect('login')
            return redirect('home')
    else:
        form = RegistrationForm()
    context = {'form': form}
    return render(request, 'account/register.html', context)


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('home')



# def create_teacher(request):
