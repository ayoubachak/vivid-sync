from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def index(request):
    return render(request, 'frontend/base.html')

# views.py
from datetime import datetime

def landing_page(request):
    return render(request, 'landing_page.html', {'current_year': datetime.now().year})

