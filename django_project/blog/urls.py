'''
2020.08.05
    urls.py
'''
from django.urls import path
from . import views

urlpatterns = [
    # path '' -> /localhost:8000/
    path('', views.post_list, name = 'post_list'),
    path('post/<int:pk>/', views.post_detail, name = 'post_detail'), # 2020.8.6
    path('edit/', views.post_edit, name='post_edit')
]