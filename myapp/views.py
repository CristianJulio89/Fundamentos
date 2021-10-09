from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from myapp.models import *
from datetime import date

# Create your views here.

def index(request):
  if not request.user.is_authenticated:
    return render(request, "index.html", {"message": None})
  context = {
    "user": request.user
  }
  return render(request, "user/index.html", context)
  
def login_view(request):
  username = request.POST["username"]
  password = request.POST["password"]
  user = authenticate(request, username=username, password=password)
  if user is not None:
    login(request, user)
    return HttpResponseRedirect(reverse("index"))
  else:
    return render(request, "index.html", {"message": "Invalid credentials."})

def logout_view(request):
  
  logout(request)
  return render(request, "index.html", {"message": "Logged out."})

def register_view(request):
  
  return render(request, "register.html")

def profile_view(request):
  if request.user.is_authenticated:
    context = {
    "user": request.user
    }
    return render(request, "user/profile.html", context)

def new_user(request):
  firstname=request.POST["firstname"]
  lastname= request.POST["lastname"]
  email=request.POST["email"]
  password=request.POST["password"]
  username= firstname+lastname

  user = User.objects.create_user(username, email , password)
  profile = Profile.objects.create(user=user, about="cuentanos de tí" ,  url="")

  user.first_name = firstname
  user.last_name = lastname
  user.save()
  user = authenticate(request, username=username, password=password)
  if user is not None:
    login(request, user)
    return HttpResponseRedirect(reverse("index"))
  return render(request, "register.html")

def edit_user(request):
  _userid = request.user.id
  user= User.objects.get(id=_userid)  
  user.first_name=request.POST["first_name"]
  user.last_name= request.POST["last_name"]
  user.email=request.POST["email"]
  user.profile.about=request.POST["about"]
  user.profile.country=request.POST["country"]
  user.profile.birthday=request.POST["birthday"]
  user.profile.profession=request.POST["profession"]
  user.profile.mobile=request.POST["mobile"]
  user.profile.url=request.POST["url"]
  user.profile.save()
  user.save()
  #user= User.objects.get(id=_userid) 
  
  return HttpResponseRedirect(reverse("profile"))

"""@login_required
def home(request):
  return render(request, 'home.html')"""
