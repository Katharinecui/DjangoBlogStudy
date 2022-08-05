# 绑定url与视图函数

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
]