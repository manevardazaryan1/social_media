from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import View
from django.urls import reverse_lazy
import os
from .forms import UserRegistrationForm


class RedirectAuthenticatedUserView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            social_media_url = os.environ.get("SOCIAL_MEDIA_URL", "/")
            return redirect(social_media_url)
        return super().get(request, *args, **kwargs)


class UserLoginView(RedirectAuthenticatedUserView, LoginView):
    template_name = "../templates/user/login.html"


class UserRegisterView(RedirectAuthenticatedUserView, CreateView):
    form_class = UserRegistrationForm
    template_name = "../templates/user/register.html"
    success_url = reverse_lazy("user:login")


class UserLogoutView(LogoutView):
    next_page = "main:index"