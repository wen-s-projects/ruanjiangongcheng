from rest_framework import serializers
from .models import Article, Tag, Comment, ArticleImage, ArticleFoodRef


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug', 'count']
        read_only_fields = ['id', 'count']


class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'article', 'author', 'author_username', 'content', 'status', 'created_at']
        read_only_fields = ['id', 'created_at']


class ArticleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleImage
        fields = ['id', 'article', 'url', 'thumb_url', 'width', 'height', 'created_at']
        read_only_fields = ['id', 'created_at']


class ArticleFoodRefSerializer(serializers.ModelSerializer):
    food_name = serializers.CharField(source='food.food_name', read_only=True)
    
    class Meta:
        model = ArticleFoodRef
        fields = ['id', 'article', 'food', 'food_record', 'food_name', 'note']
        read_only_fields = ['id']


class ArticleSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    images = ArticleImageSerializer(many=True, read_only=True)
    food_refs = ArticleFoodRefSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'author', 'author_username', 'title', 'slug', 'markdown', 'rendered_html',
                  'status', 'allow_comments', 'created_at', 'updated_at', 'tags', 'comments', 
                  'images', 'food_refs']
        read_only_fields = ['id', 'created_at', 'updated_at', 'rendered_html']


class ArticleCreateSerializer(serializers.ModelSerializer):
    tag_names = serializers.ListField(child=serializers.CharField(), write_only=True, required=False)

    class Meta:
        model = Article
        fields = ['title', 'slug', 'markdown', 'allow_comments', 'tag_names']

    def create(self, validated_data):
        tag_names = validated_data.pop('tag_names', [])
        article = Article.objects.create(**validated_data)
        
        for tag_name in tag_names:
            tag, created = Tag.objects.get_or_create(
                name=tag_name,
                defaults={'slug': tag_name.lower().replace(' ', '-')}
            )
            ArticleTag.objects.create(article=article, tag=tag)
            if created:
                tag.count = 1
            else:
                tag.count += 1
            tag.save()
        
        return article
