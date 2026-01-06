from django.contrib import admin
from .models import Article, Tag, Comment, ArticleImage, ArticleFoodRef


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'status', 'allow_comments', 'created_at']
    list_filter = ['status', 'allow_comments', 'created_at']
    search_fields = ['title', 'author__username']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'count']
    search_fields = ['name']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'article', 'author', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['article__title', 'author__username', 'content']


@admin.register(ArticleImage)
class ArticleImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'article', 'url', 'created_at']
    list_filter = ['created_at']


@admin.register(ArticleFoodRef)
class ArticleFoodRefAdmin(admin.ModelAdmin):
    list_display = ['id', 'article', 'food', 'food_record']
    list_filter = ['article', 'food']
