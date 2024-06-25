from django.shortcuts import render,HttpResponse
from users.forms import UserRegistrationForm
def index(request):
    return render(request,'index.html',{})

def logout(request):
    return render(request, 'index.html', {})

def UserLogin(request):
    return render(request, 'UserLogin.html', {})

def AdminLogin(request):
    return render(request, 'AdminLogin.html', {})

def UserRegister(request):
    form = UserRegistrationForm()
    return render(request, 'UsersRegister.html', {'form':form})

