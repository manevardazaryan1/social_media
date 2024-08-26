from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
import os

class IndexView(TemplateView):
    template_name = "../templates/main/index.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            social_media_url = os.environ.get('SOCIAL_MEDIA_URL')
            return redirect(social_media_url)
        return super().get(request, *args, **kwargs)

