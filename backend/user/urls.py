from django.urls import path
from .views import UserLoginView, UserRegisterView, UserLogoutView

app_name = "user"

urlpatterns = [
    path("login/", UserLoginView.as_view() ,name="login"),
    path("register/", UserRegisterView.as_view(), name="register"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
]