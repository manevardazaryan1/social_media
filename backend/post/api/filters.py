from django_filters import rest_framework as filters
from post.models import Post, Comment
from django.contrib.auth.models import User

class PostFilter(filters.FilterSet):
    user = filters.NumberFilter(field_name="user__id") 
    content = filters.CharFilter(lookup_expr="icontains") 
    created_at = filters.DateTimeFilter(field_name="created_at")

    class Meta:
        model = Post
        fields = ["user", "content", "created_at"]


class CommentFilter(filters.FilterSet):
    user = filters.NumberFilter(field_name="user__id")
    content = filters.CharFilter(lookup_expr="icontains")
    post = filters.NumberFilter(field_name="post__id")

    class Meta:
        model = Comment
        fields = ["user", "content", "post"]