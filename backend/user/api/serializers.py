from rest_framework import serializers
from user.models import Profile
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name")


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    profile_picture = serializers.ImageField(required=False)
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()
    followed_by = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ("user", "bio", "profile_picture", "followers_count", 
                  "following_count", "followed_by", "following")

    def get_following_count(self, obj):
        return obj.following.count()
    
    def get_followers_count(self, obj):
        return obj.followers.count()
    
    def get_followed_by(self, obj):
        serializer = UserSerializer(obj.followers.all(), many=True, context=self.context)
        return serializer.data
    
    def get_following(self, obj):
        serializer = UserSerializer(obj.following.all(), many=True, context=self.context)
        return serializer.data
