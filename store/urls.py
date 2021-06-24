from django.urls import path, re_path

from . import views

app_name='store'

urlpatterns = [

    path('', views.listing, name="listing"),
    re_path('^(?P<game_id>[0-9]+)/$', views.detail, name="detail"),
    re_path('^search/$', views.search, name="search"),
     # path('', views.index),
    ]