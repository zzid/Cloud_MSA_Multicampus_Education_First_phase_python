'''
2020.08.05
    urls.py
'''
from django.urls import path
from . import views

urlpatterns = [
    # path '' -> /localhost:8000/
    path('', views.post_list, name = 'post_list'),
]