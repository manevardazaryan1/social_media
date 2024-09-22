from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
import os
from user.views import RedirectAuthenticatedUserView

class IndexView(RedirectAuthenticatedUserView, TemplateView):
    template_name = "../templates/main/index.html"

    # def get(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         social_media_url = os.environ.get('SOCIAL_MEDIA_URL')
    #         print(f"Authenticated user redirecting to: {social_media_url}")
    #         return redirect(social_media_url)
    #     print("Unauthenticated user accessing the page")
    #     return super().get(request, *args, **kwargs)
