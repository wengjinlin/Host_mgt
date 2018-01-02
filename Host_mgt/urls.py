"""Host_mgt URL Configuration

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
from bs_mgt import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index', views.index),
    url(r'^login', views.login),
    url(r'^logout', views.logout),
    url(r'^del_host', views.del_host),
    url(r'^add_host', views.add_host),
    url(r'^_host', views._host),
    url(r'^_group', views._group),
    url(r'^del_group', views.del_group),
    url(r'^add_group', views.add_group),
]
