from django.urls import path
from .views import ProfileListAPIView, ProfileDetailAPIView, UserListAPIView, UserDetailAPIView

urlpatterns = [
    path("profiles/", ProfileListAPIView.as_view(), name="profile-list"),
    path("profiles/<int:pk>/", ProfileDetailAPIView.as_view(), name="profile-detail"),
    path("users/", UserListAPIView.as_view(), name="user-list"),
    path("users/<int:pk>/", UserDetailAPIView.as_view(), name="user-detail"),
]