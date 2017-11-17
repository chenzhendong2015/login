"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from login import views as login_views

urlpatterns = [
    url(r'^check_name/$', login_views.check_name),
    url(r'^check_email/$', login_views.check_email),
    url(r'^success/$', login_views.success),
    url(r'^logcheck/$', login_views.logcheck),
    url(r'^regcheck/$', login_views.regcheck),
    url(r'^register/', login_views.register),
    url(r'^index/', login_views.index),
    url(r'^admin/', include(admin.site.urls)),
]
