"""DataMarker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from user import views
from django.views.static import serve
from django.conf import settings
from django.conf.urls import url, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^register/$', views.register_view, name='register'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^tagPage/$', views.tag_page, name='tagPage'),
    url(r'^tagPageturn/$', views.tag_page_turn, name='tagPageTurn'),
    url(r'^faceCluster/$', views.faceShow, name='face1'),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
    url(r'^dist/(?P<path>.*)$', serve, {"document_root": settings.DIST_ROOT}),
]
