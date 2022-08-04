from django.db import models
from django.contrib.auth.models import User # 导入文章作者

# Create your models here.

# 分类
# 创建category表格，其中一列的列名为name，id列自动创建
class Category(models.Model): 
    name = models.CharField(max_length=100) # 分类名为name

# 标签
class Tag(models.Model):
    name = models.CharField(max_length=100)

# 文章
class Post(models.Model):
    title = models.CharField(max_length=70) # 文章标题
    body = models.TextField() # 文章正文
    created_time = models.DateTimeField() # 文章的创建时间
    modified_time = models.DateTimeField() # 文章的最后一次修改时间
    excerpt = models.CharField(max_length=200, blank=True) # 文章摘要

    # 关联文章对应的数据库表和分类、标签对应的数据库表
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # 一对多对应关系
    tags = models.ManyToManyField(Tag, blank=True) # 多对多关系

    author = models.ForeignKey(User, on_delete=models.CASCADE) # 一对多