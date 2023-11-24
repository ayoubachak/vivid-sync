from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.


def index(request):
    return render(request, 'frontend/auth/base.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('/me/')
    return render(request, 'frontend/auth/login.html')

def signup(request):
    return render(request, 'frontend/auth/signup.html')

@login_required(login_url='/login/')  # Redirect to login if not authenticated
def me(request):
    """
    Redirects the user to the /profile page if authenticated.
    """
    user = request.user
    print(user)
    context = {
        'user': user,
        'current_year': datetime.now().year,  # Example of additional context
    }
    return render(request, 'profile/profile.html', context=context)


def custom_logout(request):
    # Delete the token here if stored in server or invalidate it
    # For example, you might have a model to store tokens
    
    # Clear the session
    logout(request)

    # Redirect to home page or send a response
    return redirect('/')

# views.py
from datetime import datetime

def landing_page(request):
    return render(request, 'landing_page.html', {'current_year': datetime.now().year})

