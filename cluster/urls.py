from django.contrib import admin
from user import views
from django.views.static import serve
from django.conf import settings
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.ImageList),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),

]
