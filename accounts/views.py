from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from django.contrib import messages
from .models import Profile

def signup_view(request):
    if request.method=="POST":
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect("home")
    else:
        form=CustomUserCreationForm()

    context={
        "form":form
    }
    return render(request,"signup.html",context)

def signin_view(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect("home")
    else:
        form=AuthenticationForm()
    context={
        "form":form
    }
    return render(request,"login.html",context)

def logout_view(request):
    logout(request)
    return redirect("login")


def profile_page(request,pk):
    profile=get_object_or_404(Profile,id=pk)
    context={"profile":profile}
    return render(request,"profile1.html",context)



