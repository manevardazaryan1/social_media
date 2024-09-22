from django.db import models
from django.contrib.auth.models import User
from post.helpers import upload_image

class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE,)
    content = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=upload_image, blank=True, null=True)
    likes = models.ManyToManyField(User, related_name="liked_posts",blank=True)
    saved_by = models.ManyToManyField(User, related_name="saved_posts",blank=True)

    def __str__(self):
        """Post class str function"""
        return self.content


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Comment class str function"""
        return self.content