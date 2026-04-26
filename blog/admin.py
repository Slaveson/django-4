

from django.contrib import admin
from .models import Post, Comments


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug', 'author', 'publish','status']
    list_filter = ['status', 'publish', 'author', 'created']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['publish', 'status']

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'body', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']
