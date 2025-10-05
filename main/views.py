from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'html/index.html')

def Aldult_English(request):
    return render(request, 'html/adultenglish/Adult_English.html')

def Aldult_English1(request):
    return render(request, 'html/adultenglish/Adult_English1.html')

def Aldult_English2(request):
    return render(request, 'html/adultenglish/Adult_English2.html')

def Children_English(request):
    return render(request, 'html/chidrenenglish/Children_English.html')

def Children_English1(request):
    return render(request, 'html/chidrenenglish/Children_English1.html')

def Children_English2(request):
    return render(request, 'html/chidrenenglish/Children_English2.html')

def ielts(request):
    return render(request, 'html/ietls/ielts.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = CreateUserForm
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'html/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username  = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password) 
        print(user)  # kiểm tra xem user có tồn tại không
        # kiểm tra xem user có tồn tại không
        if user is not None:
            login(request, user)
            print('Login successfully')
            return redirect('home')
        else: messages.info(request,'Username or password is incorrect')
    form = UserCreationForm()
    context = {'form':form}
    return render(request, 'html/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('home')

def unit1(request):
    return render(request, 'html/chidrenenglish/unit1.html')

def unit2(request):
    return render(request, 'html/chidrenenglish/unit2.html')

def unit3(request):
    return render(request, 'html/chidrenenglish/unit3.html')

def unit4(request):
    return render(request, 'html/chidrenenglish/unit4.html')

def unit5(request):
    return render(request, 'html/chidrenenglish/unit5.html')

def unit6(request):
    return render(request, 'html/chidrenenglish/unit6.html')

def unit7(request):
    return render(request, 'html/chidrenenglish/unit7.html')

def unit8(request):
    return render(request, 'html/chidrenenglish/unit8.html')

def unit9(request):
    return render(request, 'html/chidrenenglish/unit9.html')