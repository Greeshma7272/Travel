from django.shortcuts import render
from .models import Place, Meet


# Create your views here.
def temp(request):
    obj=Place.objects.all()
    inf = Meet.objects.all()
    return render(request,'index.html',{'object':obj,'info':inf})


# def post(request):
#     inf = Meet.objects.all()
#     return render(request,'index.html',{'info':inf})