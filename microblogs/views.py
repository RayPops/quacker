from django.shortcuts import render, redirect
from .forms import LogInForm, SignupForm
from django.contrib.auth import authenticate, login

# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def feed_view(request):
    return render(request, 'feed.html')

def login_view(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('feed')
    else:
        form = LogInForm()
    return render(request, 'login.html', {'form': form})