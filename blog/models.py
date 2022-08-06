from django.db import models
from django.contrib.auth.models import User # 导入文章作者
from django.utils import timezone # 导入时间模块
from django.urls import reverse
import markdown
from django.utils.html import strip_tags

# Create your models here.

# 分类
# 创建category表格，其中一列的列名为name，id列自动创建
class Category(models.Model): 
    name = models.CharField(max_length=100) # 分类名为name

    class Meta: # 后台汉化
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 标签
class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta: # 后台汉化
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 文章
class Post(models.Model):
    title = models.CharField('标题', max_length=70) # 文章标题
    body = models.TextField('正文') # 文章正文
    created_time = models.DateTimeField('创建时间', default=timezone.now) # 文章的创建时间
    modified_time = models.DateTimeField('修改时间') # 文章的最后一次修改时间
    excerpt = models.CharField('摘要', max_length=200, blank=True) # 文章摘要

    # 关联文章对应的数据库表和分类、标签对应的数据库表
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE) # 一对多对应关系
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True) # 多对多关系

    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE) # 一对多

    class Meta: # 后台汉化
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs): # 自动填充修改时间
        self.modified_time = timezone.now()

        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])
        self.excerpt = strip_tags(md.convert(self.body))[:54]
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    # 自定义 get_absolute_url 方法
    # 记得从 django.urls 中导入 reverse 函数
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})