from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect, HttpResponseRedirect, render
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import View
from django.urls import reverse_lazy
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json
import os
from user.form import LoginForm
from .forms import UserRegistrationForm
from django.core.cache import cache
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from rest_framework.permissions import BasePermission
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class RedirectAuthenticatedUserView(View):
    def get(self, request, *args, **kwargs):
        # Check if user is authenticated
        if request.user.is_authenticated and cache.get('jwt'):
            # Redirect to the social media URL if authenticated
            social_media_url = os.environ.get("SOCIAL_MEDIA_URL", "/")
            return redirect(social_media_url)
        # Otherwise, render the requested page
        return super().get(request, *args, **kwargs)

class UserLoginView(RedirectAuthenticatedUserView):
    template_name = "../templates/user/login.html"

    def get(self, request, *args, **kwargs):
        # Render the login form
        if request.user.is_authenticated and cache.get('jwt'):
            # Redirect to the social media URL if authenticated
            social_media_url = os.environ.get("SOCIAL_MEDIA_URL", "/")
            return redirect(social_media_url)
        form = self.get_form()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        # Retrieve username and password from POST data
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Authenticate the user
        user = authenticate(username=username, password=password)
        
        if user is not None:
            # Log the user in
            login(request, user)
            # Create a refresh token and cache it
            refresh = RefreshToken.for_user(user)
            cache.set('jwt', str(refresh.access_token), timeout=86400)  # Cache for 24 hours
            cache.set('user', str(request.user.id), timeout=86400)  # Cache for 24 hours
            
            # Redirect to the social media URL
            social_media_url = os.environ.get("SOCIAL_MEDIA_URL", "/")
            return redirect(social_media_url)
        
        # If authentication fails, re-render the login form with an error message
        form = self.get_form(username)
        context = {'form': form, 'error_message': 'Invalid credentials'}
        return render(request, self.template_name, context)

    def get_form(self, username=None):
        # Initialize the login form with the provided username (if any)
        form = LoginForm(initial={'username': username})
        return form

# class RedirectAuthenticatedUserView(View):
#     def get(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             social_media_url = os.environ.get("SOCIAL_MEDIA_URL", "/")
#             return redirect(social_media_url)
#         return super().get(request, *args, **kwargs)


# class UserLoginView(RedirectAuthenticatedUserView, LoginView):
#     template_name = "../templates/user/login.html"

#     def get(self, request, *args, **kwargs):
#         form = self.get_form()
#         return render(request, self.template_name, {'form': form})

#     def post(self, request, *args, **kwargs):
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             refresh = RefreshToken.for_user(user)
#             cache.set('jwt', str(refresh.access_token), timeout=86400)

#             return redirect(os.environ.get("SOCIAL_MEDIA_URL"))
        
#         form = self.get_form(request.POST.get('username'))
#         context = {'form': form, 'error_message': 'Invalid credentials'}
#         return render(request, self.template_name, context)

#     def get_form(self, username=None):
#         form = LoginForm(initial={'username': username})
#         return form     
 

class UserRegisterView(RedirectAuthenticatedUserView, CreateView):
    form_class = UserRegistrationForm
    template_name = "../templates/user/register.html"
    success_url = reverse_lazy("user:login")


class UserLogoutView(LogoutView):
    next_page = 'main:index'

    def get(self, request, *args, **kwargs):
        cache.delete('jwt')
        return super().get(request, *args, **kwargs)


class IsAuthenticatedClient(BasePermission):
    def has_permission(self, request, view):
        # Allow only authenticated users
        if not request.user.is_authenticated:
            return False

        # Optionally, check for a custom header or referer (sent by React frontend)
        referer = request.headers.get('Referer', '')
        if 'your-frontend-url' not in referer:
            return False

        return True

from rest_framework.permissions import BasePermission

class IsTokenOwner(BasePermission):
    def has_permission(self, request, view):
        token = cache.get('jwt')
        # Only allow access if the user is authenticated and the token exists
        return token is not None and request.user.is_authenticated

class GetTokenView(View):
    permission_classes = [IsAuthenticated]
    @csrf_exempt
    def get(self, request, *args, **kwargs):
        if request.headers.get('X-Requested-With') != 'XMLHttpRequest':
            return JsonResponse({'error': 'Unauthorized access'}, status=status.HTTP_403_FORBIDDEN)
        
        jwt = cache.get('jwt')
        user = cache.get('user')
        return JsonResponse({'token': jwt, "user": user})
    
# def test_session(request):
#     if request.method == 'POST':
#         request.session['test_key'] = 'test_value'
#         return JsonResponse({'status': 'Session value set'})
#     elif request.method == 'GET':
#         test_value = request.session.get('test_key', None)
#         return JsonResponse({'test_key': test_value})