from django.contrib import admin
from .models import Post, Category, Tag

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author'] # 定制后台文章列表页面
    fields = ['title', 'body', 'excerpt', 'category', 'tags'] # Post表单展示字段

    def save_model(self, request, obj, form, change): # 自动填充作者
        obj.author = request.user
        super().save_model(request, obj, form, change)

# admin后台注册模型
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)