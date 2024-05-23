from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    context={}
    return render(request, 'FerremaxWeb/index.html', context)

def store(request):
    context={}
    return render(request, 'FerremaxWeb/store.html', context)

def login(request):
    if request.method == 'GET':
        return render(request, 'FerremaxRegistro/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is None:
            return render(request, 'FerremaxRegistro/login.html', {
                'form': AuthenticationForm(),
                'error': 'Username o contraseña incorrecta'
            })
        else:
            login(request, user)
            return redirect('index')

def register(request):
    if request.method == 'GET':
        return render(request, 'FerremaxRegistro/register.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
                try:
                    user = User.objects.create_user(
                    username=request.POST['username'],
                    password =request.POST['password1'])
                    user.save()
                    login(request, user)
                    return redirect('index')
                except IntegrityError:
                    return render(request, 'FerremaxRegistro/register.html', {
                    'form': UserCreationForm,
                    "error" : 'Usuario ya existe'
                })
            
        return render(request, 'FerremaxRegistro/register.html', {
                    'form': UserCreationForm,
                    "error" : 'La contraseña no coincide'
                })