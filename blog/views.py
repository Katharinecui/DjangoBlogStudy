from django.shortcuts import render

# Create your views here.
# 视图函数

from django.http import HttpResponse

def index(request):
    return HttpResponse("欢迎访问我的博客首页！")