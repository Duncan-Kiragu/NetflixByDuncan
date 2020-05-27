from django.conf.urls import re_path
from . import views,api

urlpatterns = [
    re_path(r'^$', views.home, name = 'index'),
    re_path(r'^login/$', views.login, name='login')




]