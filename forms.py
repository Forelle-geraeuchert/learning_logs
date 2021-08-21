# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 15:47:26 2021

@author: luy
"""

from django import forms

from .models import Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ' '}