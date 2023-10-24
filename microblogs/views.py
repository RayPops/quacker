from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignupForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup_view(request):
    form = SignupForm()
    return render(request, 'signup.html', {'form': form})