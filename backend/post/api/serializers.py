from rest_framework import serializers
from post.models import Post, Comment
from user.api.serializers import UserSerializer
from django.contrib.auth.models import User

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Comment
        fields = ("id", "user", "post", "content", "created_at")


class PostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    user_id = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    is_saved = serializers.SerializerMethodField()
    liked_by = serializers.SerializerMethodField()
    saved_by = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ["id", "user", "user_id", "content", "created_at", "image", 
                  "likes_count", "is_liked", "comments", "liked_by", "saved_by", "is_saved"]

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_is_liked(self, obj):
        user = obj.user
        if user.is_authenticated:
            return obj.likes.filter(id=user.id).exists()
        return False
    
    def get_is_saved(self, obj):
        user = obj.user
        if user.is_authenticated:
            return obj.likes.filter(id=user.id).exists()
        return False
    
    def get_user_id(self, obj):
        return obj.user.id
    

    def get_liked_by(self, obj):
        serializer = UserSerializer(obj.likes.all(), many=True, context=self.context)
        return serializer.data
    
    def get_saved_by(self, obj):
        serializer = UserSerializer(obj.saved_by.all(), many=True, context=self.context)
        return serializer.data