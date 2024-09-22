from django.urls import path
from .views import UserLoginView, UserRegisterView, UserLogoutView, GetTokenView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

app_name = "user"

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/verify-token/', TokenVerifyView.as_view(), name='verify-token'),
    path('api/get-token/', GetTokenView.as_view(), name='get-token'),
    path("login/", UserLoginView.as_view() ,name="login"),
    path("register/", UserRegisterView.as_view(), name="register"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    # path('test', test_session, name="test")
]