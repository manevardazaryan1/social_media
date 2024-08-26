from django.db import models
from django.contrib.auth.models import User
from user.helpers import upload_image
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to=upload_image, blank=True, null=True)
    following = models.ManyToManyField(User, related_name="followers", blank=True)
    followers = models.ManyToManyField(User, related_name="following", blank=True)

    def __str__(self):
        """Profile class str function"""
        return self.user.username
     

class ProfileSignalHandler:
    @staticmethod
    @receiver(post_save, sender=User)
    def send_profile_signal(sender, instance, created, **kwargs):
        """Profile creation function"""
        if created:
            Profile.objects.create(user=instance)
            instance.profile.save()