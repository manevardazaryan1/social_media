from rest_framework import serializers
from user.models import Profile
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    bio = serializers.SerializerMethodField()
    profile_picture = serializers.SerializerMethodField()
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()
    followed_by = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email", "bio", "followed_by", "following", 
                  "following_count", "followers_count", "profile_picture")
    
    def get_profile_picture(self, obj):
        request = self.context.get('request')
        domain = f"{request.scheme}://{request.get_host()}"
        picture_url = Profile.objects.get(user=obj).profile_picture
        if picture_url:
            return  f"{domain}/{picture_url.url}"
        return ""
    
    def get_followers_count(self, obj):
        return  Profile.objects.get(user=obj).followers.count()
    
    def get_following_count(self, obj):
        return  Profile.objects.get(user=obj).following.count()
    
    def get_bio(self, obj):
        return  Profile.objects.get(user=obj).bio
    
    def get_followed_by(self, obj):
        try:
            followers = Profile.objects.get(user=obj).followers.all()
            return UserSerializer(followers, many=True, context=self.context).data
        except Profile.DoesNotExist:
            return []

    def get_following(self, obj):
        try:
            following = Profile.objects.get(user=obj).following.all()
            return UserSerializer(following, many=True, context=self.context).data
        except Profile.DoesNotExist:
            return []
    
class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()
    followed_by = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ("user", "bio", "first_name", "last_name", "profile_picture", "followers_count", 
                  "following_count", "followed_by", "following", "username", "email")

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
    
    def get_username(self, obj):
        return obj.user.username
    
    def get_first_name(self, obj):
        return obj.user.first_name
    
    def get_last_name(self, obj):
        return obj.user.last_name
    
    def get_email(self, obj):
        return obj.user.email