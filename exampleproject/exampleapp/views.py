from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import projecetable
from .models import table2


# Create your views here.
def home(request):
    o = projecetable.objects.all()
    ob = table2.objects.all()
    return render(request, "index.html", {'result': o, 'answer': ob})


def log(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('log')
    return render(request, "index2.html")


def regis(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpass = request.POST['cpass']
        if password == cpass:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exists")
                return redirect('regis')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                return redirect('regis')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
                messages.info(request,"Registation successfull")
                return redirect('log')

        else:
            messages.info(request, "Password and confirm password should be same.")
            return redirect('regis')
        return redirect('/')
    return render(request,"index3.html")


def lout(request):
    auth.logout(request)
    return redirect('/')