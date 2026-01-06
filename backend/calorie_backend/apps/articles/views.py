from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db.models import Q
from .models import Article, Tag, Comment, ArticleImage, ArticleFoodRef
from .serializers import (ArticleSerializer, ArticleCreateSerializer, TagSerializer, 
                          CommentSerializer, ArticleImageSerializer, ArticleFoodRefSerializer)


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.filter(status='published')
    serializer_class = ArticleSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ArticleCreateSerializer
        return ArticleSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated()]
        return [AllowAny()]

    def get_queryset(self):
        queryset = super().get_queryset()
        tag_slug = self.request.query_params.get('tag')
        search = self.request.query_params.get('search')
        
        if tag_slug:
            queryset = queryset.filter(tags__slug=tag_slug)
        
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | Q(markdown__icontains=search)
            )
        
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=False, methods=['get'])
    def my_articles(self, request):
        articles = Article.objects.filter(author=request.user)
        serializer = self.get_serializer(articles, many=True)
        return Response(serializer.data)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [AllowAny]

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [IsAuthenticated()]
        return [AllowAny()]

    @action(detail=True, methods=['get'])
    def articles(self, request, pk=None):
        tag = self.get_object()
        articles = tag.article_set.filter(status='published')
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.filter(status='active')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        article_id = self.request.query_params.get('article')
        if article_id:
            return Comment.objects.filter(article_id=article_id, status='active')
        return super().get_queryset()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ArticleImageViewSet(viewsets.ModelViewSet):
    queryset = ArticleImage.objects.all()
    serializer_class = ArticleImageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class ArticleFoodRefViewSet(viewsets.ModelViewSet):
    queryset = ArticleFoodRef.objects.all()
    serializer_class = ArticleFoodRefSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()
