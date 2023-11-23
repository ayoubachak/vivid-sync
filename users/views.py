from django.shortcuts import render

# Create your views here.
import jwt
from django.conf import settings
from django.contrib.auth import authenticate
from django.http import JsonResponse
from datetime import datetime, timedelta
from .models import VividUser

def generate_token(user):
    payload = {
        'user_id': user.id,
        'exp': datetime.utcnow() + timedelta(days=1),
        'iat': datetime.utcnow()
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

def obtain_jwt_token(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user:
        return JsonResponse({'token': generate_token(user)})
    return JsonResponse({'error': 'Invalid Credentials'}, status=400)

def refresh_token(request):
    refresh_token = request.POST.get('refresh_token')
    try:
        payload = jwt.decode(refresh_token, settings.SECRET_KEY, algorithms=['HS256'])
        user = VividUser.objects.get(id=payload['user_id'])

        # Check if the refresh token has expired
        if payload['exp'] < datetime.utcnow().timestamp():
            return JsonResponse({'error': 'Refresh token expired'}, status=400)

        new_token = generate_token(user)
        return JsonResponse({'token': new_token})
    except jwt.ExpiredSignatureError:
        return JsonResponse({'error': 'Refresh token expired'}, status=400)
    except jwt.DecodeError:
        return JsonResponse({'error': 'Invalid token'}, status=400)
    except VividUser.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
