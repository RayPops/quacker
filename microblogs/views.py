from django.shortcuts import render, redirect
from .forms import SignupForm

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
    return render(request, 'login.html')