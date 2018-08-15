# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r"^(?P<task_type>(add|minus|multiply|divide))/(?P<x>(-?\d+)(\.?\d*))/(?P<y>(-?\d+)(\.?\d*))/?$", views.index),
    path('query/', views.query),
    url(r'^$', views.index),
]
