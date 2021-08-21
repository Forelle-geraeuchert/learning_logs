# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 10:07:57 2021

@author: luy
"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name='index'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    ]