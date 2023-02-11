from django.contrib import admin
from .models import Post, Category, Like

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Like)
