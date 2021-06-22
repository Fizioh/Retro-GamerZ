from django.urls import path, re_path

from . import views

urlpatterns = [

    path('', views.listing),
    re_path('^(?P<game_id>[0-9]+)/$', views.detail),
    re_path('^search/$', views.search),
     # path('', views.index),
    ]