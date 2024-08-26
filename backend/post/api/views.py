from rest_framework import generics
from .serializers import PostSerializer, CommentSerializer
from .filters import PostFilter, CommentFilter
from .permissions import IsAdminOrReadOnly
from post.models import Post, Comment

class PostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filterset_class = PostFilter
    permission_classes = [IsAdminOrReadOnly]


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminOrReadOnly]


class CommentListAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filterset_class = CommentFilter
    permission_classes = [IsAdminOrReadOnly]


class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminOrReadOnly]