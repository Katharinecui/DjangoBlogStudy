# 绑定url与视图函数

from django.urls import path
from . import views

app_name = 'blog' # 视图函数命名空间
urlpatterns = [
    path('', views.index, name = 'index'),
    path('posts/<int:pk>/', views.detail, name='detail'), # 每篇文章的URL规则
]