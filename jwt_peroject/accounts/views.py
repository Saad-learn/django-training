from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model
from django.http import JsonResponse
from .utils import generate_jwt, decode_jwt
import jwt

User = get_user_model()

def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            return JsonResponse({'error': 'Missing fields'}, status=400)

        User.objects.create_user(username=username, password=password)
        return redirect('login')

    return render(request, 'register.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            return JsonResponse({'error': 'Missing credentials'}, status=400)

        user = authenticate(username=username, password=password)
        if not user:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)

        token = generate_jwt(user)
        response = redirect('dashboard')
        response.set_cookie('jwt', token)
        return response

    return render(request, 'login.html')


def logout_view(request):
    response = redirect('login')
    response.delete_cookie('jwt')
    return response


def dashboard_view(request):
    token = request.COOKIES.get('jwt')

    if not token:
        return redirect('login')

    try:
        payload = decode_jwt(token)
    except jwt.ExpiredSignatureError:
        return redirect('login')
    except jwt.InvalidTokenError:
        return redirect('login')

    return render(request, 'dashboard.html', {
        'username': payload['username']
    })
