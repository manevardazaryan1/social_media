from django_filters import rest_framework as filters
from user.models import Profile
from django.contrib.auth.models import User

class ProfileFilter(filters.FilterSet):
    user = filters.NumberFilter(field_name="user__id")

    class Meta:
        model = Profile
        fields = ["user"]


class UserFilter(filters.FilterSet):
    username = filters.CharFilter(lookup_expr="icontains")
    email = filters.CharFilter(lookup_expr="icontains")

    first_name = filters.CharFilter(lookup_expr="icontains")
    last_name = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]