from django.shortcuts import render
from .forms import LoginForm, RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

# Create your views here.
def login_view(request):
    if request.method=="POST":
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')

    else:
        form = LoginForm()
        return render(request, "account.html", {"form":form})

def logout_view(request):
    logout(request)
    return redirect("home")

def register_view(request):
    if request.method=="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        return render(request, "account.html", {"form":form})

    else:
        form = RegisterForm()
        return render(request, "account.html", {"form":form})

