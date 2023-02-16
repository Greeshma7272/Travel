from django.contrib import messages, auth
from django.contrib.auth.models import User
# from django.http import request
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalied credentials')
            return redirect('login')
    return render(request, "login.html")

        # else:
        #     user=User.objects.create_user(username=username,password=password)
        #
        #
        #     user.save();
        #



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        lastname = request.POST['LastName']
        email = request.POST['Email']
        password = request.POST['Password']
        password1 = request.POST['Password1']
        user = User.objects.create_user(username=username,password=password,last_name=lastname,email=email)
        user.save();
        return redirect('login')
    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return  redirect('/')
