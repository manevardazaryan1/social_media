from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from django.urls import re_path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("user/", include("user.urls")),
    path("api/v1/user/", include("user.api.urls")),
    path("api/v1/post/", include("post.api.urls")),
    path("api/v1/message/", include("message.api.urls")),
]

urlpatterns += [
    re_path(r"^media/(?P<path>.*)$", serve, {
        "document_root": settings.MEDIA_ROOT,
    }),
]

urlpatterns += staticfiles_urlpatterns()