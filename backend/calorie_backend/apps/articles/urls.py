from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (ArticleViewSet, TagViewSet, CommentViewSet, 
                     ArticleImageViewSet, ArticleFoodRefViewSet)

router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='article')
router.register(r'tags', TagViewSet, basename='tag')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'article-images', ArticleImageViewSet, basename='articleimage')
router.register(r'article-food-refs', ArticleFoodRefViewSet, basename='articlefoodref')

urlpatterns = [
    path('', include(router.urls)),
]
