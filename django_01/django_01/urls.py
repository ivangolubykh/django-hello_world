"""django_01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from indexapp.views import *
from django.views.generic.base import RedirectView # для редиректа с главной страницы в папку

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(url='django/profile_ig/')), # редирект с главной страницы в папку
    url(r'^django/profile_ig/', include([
        url(r'^$', index, name='index'),
        url(r'^learn/$', learn, name='learn'),
        url(r'^work/$', work, name='work'),
    ])),
]
