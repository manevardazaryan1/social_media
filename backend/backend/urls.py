from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from django.urls import re_path

urlpatterns = [
    path("", include("main.urls")),
    path("admin/", admin.site.urls), 
] 

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]

urlpatterns += staticfiles_urlpatterns()
