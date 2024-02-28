from django.shortcuts import render
from django.http import HttpResponse
from .models import Shoes

def home(request):
    shoes = Shoes.objects.all()
    return render(request,"home.html",{"shoes":shoes})
def login(request):
    return render(request,"login.html")
def signup(request):
    return render(request,"signup.html")