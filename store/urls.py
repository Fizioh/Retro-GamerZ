from django.urls import path

from . import views

urlpatterns = [

    path('', views.listing),
     # path('', views.index),
    ]