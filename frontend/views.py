from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from registration.utils import send_verification_email
from rest_framework.response import Response
from django.views.decorators.csrf import ensure_csrf_cookie

def index(request):
    return render(request, 'frontend/auth/base.html')

@ensure_csrf_cookie
def login(request):
    if request.user.is_authenticated:
        return redirect('/me/')
    return render(request, 'frontend/auth/login.html')

def signup(request):
    return render(request, 'frontend/auth/signup.html')

def password_reset(request, uidb64, token):
    # You can use uidb64 and token here if needed, 
    # or simply pass them to the template.
    return render(request, 'frontend/auth/password_reset.html', {'uidb64': uidb64, 'token': token})

def forgot_password(request):
    return render(request, 'frontend/auth/forgot_password.html')

@login_required(login_url='/login/')
def verify_email(request):
    user = request.user
    if user.email_verified:
        # check if the user agreed to the terms, if not redirect him to the terms of service page 
        if not user.agreed_to_terms:
            return redirect('/terms-of-service/')
        return redirect('/me/')
    return render(request, 'frontend/auth/verify_email.html')

@login_required(login_url='/login/')
def terms_of_service(request):
    return render(request, 'frontend/auth/terms_of_service.html')

@login_required(login_url='/login/')  # Redirect to login if not authenticated
def me(request):
    """
    Redirects the user to the /profile page if authenticated.
    """
    from django.utils.crypto import get_random_string
    user = request.user
    context = {
        'user': user,
        'current_year': datetime.now().year,  # Example of additional context
    }
    if not user.email_verified:
        if not user.verification_code or not user.verification_token:
            # If not, generate them now and send a verification email
            user.verification_code = get_random_string(length=6, allowed_chars='1234567890')
            user.verification_token = get_random_string(length=100)
            user.save(update_fields=['verification_code', 'verification_token'])
            send_verification_email(user, request)
        return redirect('/signup/verify-email/')
    if not user.agreed_to_terms:
        return redirect('/terms-of-service/')
    if not user.profile_completed :
        return redirect('/complete-profile/') 

    return render(request, 'profile/profile.html', context=context)

from rest_framework import status

@login_required(login_url='/login/')
def setup_account_type(request):
    # Logic for setting up account type
    return render(request, 'frontend/profile/setup_account_type.html')

@login_required(login_url='/login/')
def setup_personal_info(request):
    # Logic for completing personal information
    return render(request, 'frontend/profile/setup_personal_info.html')

@login_required(login_url='/login/')
def congratulations(request):
    # Logic for serving the congratulations page
    return render(request, 'frontend/profile/setup_congratulations.html')

@login_required(login_url='/login/')
def last_steps(request):
    # Logic for serving the last steps page
    return render(request, 'frontend/profile/setup_social_links.html')


@login_required(login_url='/login/')
def complete_profile(request):
    user = request.user
    if not user.profile_completed:
        return redirect('/complete-profile/personal-info/')
    # Redirect to some other view if the account type is set and profile is completed
    return redirect('/me/')

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
    return render(request, 'pages/landing_page.html', {'current_year': datetime.now().year})
def about_page(request):
    return render(request, 'pages/about_page.html', {'current_year': datetime.now().year})
def pricing_page(request):
    return render(request, 'pages/pricing_page.html', {'current_year': datetime.now().year})
def tools_page(request):
    return render(request, 'pages/tools_page.html', {'current_year': datetime.now().year})


## Dashboard views
@login_required(login_url='/login/')
def accounts_view(request):
    return render(request, 'frontend/dashboard/accounts.html')

@login_required(login_url='/login/')
def ads_view(request):
    return render(request, 'frontend/dashboard/ads.html')

@login_required(login_url='/login/')
def analyze_view(request):
    return render(request, 'frontend/dashboard/analyze.html')

@login_required(login_url='/login/')
def create_view(request):
    return render(request, 'frontend/dashboard/create.html')

@login_required(login_url='/login/')
def dashboard_view(request):
    return render(request, 'frontend/dashboard/dashboard.html')

@login_required(login_url='/login/')
def feed_view(request):
    return render(request, 'frontend/dashboard/feed.html')

@login_required(login_url='/login/')
def inbox_view(request):
    return render(request, 'frontend/dashboard/inbox.html')

@login_required(login_url='/login/')
def schedule_view(request):
    return render(request, 'frontend/dashboard/schedule.html')

@login_required(login_url='/login/')
def teams_view(request):
    return render(request, 'frontend/dashboard/teams.html')


@login_required(login_url='/login/')
def general_settings(request):
    return render(request, 'frontend/settings/general_settings.html')


