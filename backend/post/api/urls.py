from django.urls import path
from .views import PostListAPIView, PostDetailAPIView, CommentListAPIView, CommentDetailAPIView

urlpatterns = [
    path("posts/", PostListAPIView.as_view(), name="post-list"),
    path("posts/<int:pk>/", PostDetailAPIView.as_view(), name="post-detail"),
    path("posts/<int:post_pk>/comments/", CommentListAPIView.as_view(), name="comment-list"),
    path("posts/<int:post_pk>/comments/<int:pk>/", CommentDetailAPIView.as_view(), name="comment-detail"),
]