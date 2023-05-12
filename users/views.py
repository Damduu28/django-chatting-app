from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import RegisterUserForm, ProfileUpdateForm
from .models import User

# Create your views here.

def loginUser(request):
    
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request,"User does not exist.!!!")
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            user.status = "Active now"
            user.save()
            return redirect('home')
        else:
            messages.error(request, "Email Or Password is invalid.!!!")
    context = {'page': 'login'}
    return render(request, "users/register_login.html", context)

def logoutUser(request):
    request.user.status = "Not Active"
    request.user.save()
    logout(request)
    return redirect('login')

def registerUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = request.POST.get('username').lower()
            user.save()
            return redirect('login')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    else:
        form = RegisterUserForm()
    context = {'form': form}
    return render(request, "users/register_login.html", context)

@login_required(login_url="login")
def updateProfile(request, pk):
    user = User.objects.get(id=pk)
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileUpdateForm(instance=user)
    
    context = {"form": form}
    return render(request, "users/update_profile.html", context)
    
    


