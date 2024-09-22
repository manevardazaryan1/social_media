from rest_framework import generics
from user.models import Profile
from .serializers import ProfileSerializer, UserSerializer
from .filters import ProfileFilter, UserFilter
from .permissions import IsAdminOrReadOnly, IsAuthenticatedOrReadOnly
from .paginators import MyOffsetPagination
from django.contrib.auth.models import User
from rest_framework.parsers import MultiPartParser

class ProfileListAPIView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filterset_class = ProfileFilter
    pagination_class = MyOffsetPagination
    permission_classes = []

class ProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer 
    permission_classes = []
    parser_classes = [MultiPartParser]


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilter
    pagination_class = MyOffsetPagination
    permission_classes = []


class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []
    parser_classes = [MultiPartParser]