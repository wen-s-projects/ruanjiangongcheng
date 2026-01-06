from django.db import models
from apps.users.models import User, FoodDict, FoodRecord


class ArticleStatus(models.TextChoices):
    DRAFT = 'draft', '草稿'
    PUBLISHED = 'published', '已发布'
    DELETED = 'deleted', '已删除'


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles', verbose_name='作者')
    title = models.CharField(max_length=200, verbose_name='标题')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='URL别名')
    markdown = models.TextField(verbose_name='Markdown内容')
    rendered_html = models.TextField(verbose_name='渲染后的HTML')
    status = models.CharField(max_length=20, choices=ArticleStatus.choices, default=ArticleStatus.DRAFT, verbose_name='状态')
    allow_comments = models.BooleanField(default=True, verbose_name='允许评论')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table = 'Article'
        verbose_name = '文章'
        verbose_name_plural = '文章'
        ordering = ['-created_at']


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='标签名称')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='URL别名')
    count = models.IntegerField(default=0, verbose_name='文章数量')

    class Meta:
        db_table = 'Tag'
        verbose_name = '标签'
        verbose_name_plural = '标签'


class ArticleTag(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='文章')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='标签')

    class Meta:
        db_table = 'ArticleTag'
        unique_together = ['article', 'tag']
        verbose_name = '文章标签'
        verbose_name_plural = '文章标签'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name='文章')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='comments', verbose_name='作者')
    content = models.TextField(verbose_name='评论内容')
    status = models.CharField(max_length=20, default='active', verbose_name='状态')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        db_table = 'Comment'
        verbose_name = '评论'
        verbose_name_plural = '评论'
        ordering = ['-created_at']


class ArticleImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='images', verbose_name='文章')
    url = models.CharField(max_length=500, verbose_name='图片URL')
    thumb_url = models.CharField(max_length=500, null=True, blank=True, verbose_name='缩略图URL')
    width = models.IntegerField(null=True, blank=True, verbose_name='宽度')
    height = models.IntegerField(null=True, blank=True, verbose_name='高度')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        db_table = 'ArticleImage'
        verbose_name = '文章图片'
        verbose_name_plural = '文章图片'


class ArticleFoodRef(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='food_refs', verbose_name='文章')
    food = models.ForeignKey(FoodDict, on_delete=models.CASCADE, null=True, blank=True, verbose_name='食物')
    food_record = models.ForeignKey(FoodRecord, on_delete=models.CASCADE, null=True, blank=True, verbose_name='食物记录')
    note = models.TextField(null=True, blank=True, verbose_name='备注')

    class Meta:
        db_table = 'ArticleFoodRef'
        verbose_name = '文章食物引用'
        verbose_name_plural = '文章食物引用'
