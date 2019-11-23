from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from ckeditor.fields import RichTextField


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', verbose_name='头像', default='avatar/default.jpg')
    phone = models.CharField(max_length=11, unique=True, blank=False, verbose_name='手机号码')
    wechat = models.CharField(max_length=11, unique=True, blank=False, verbose_name='微信')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '所有用户'
        # 表名
        db_table = 'user'
        # 排序
        ordering = ['-id']

    def __str__(self):
        return self.username


class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name='标题名称')

    class Meta:
        db_table = 'tag'
        verbose_name = '标签'
        verbose_name_plural = '所有标签'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='分类名称')

    class Meta:
        db_table = 'category'
        verbose_name = '分类'
        verbose_name_plural = '所有分类'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=30, verbose_name='文章标题', unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    desc = models.CharField(max_length=120, verbose_name='文章摘要')
    body = RichTextField(verbose_name='文章主体')
    read_count = models.IntegerField(default=0, verbose_name='阅读次数')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='文章分类')
    tag = models.ManyToManyField(Tag, verbose_name='文章标签')

    class Meta:
        db_table = 'article'
        verbose_name = '文章'
        verbose_name_plural = '所有文章'
        ordering = ['-date_publish']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        self.count()
        return reverse('blog:art', args=[self.id])

    def count(self):
        self.read_count += 1
        self.save(update_fields=['read_count'])


class Comment(models.Model):
    title = models.CharField(max_length=30, verbose_name='评论标题')
    body = RichTextField(verbose_name='评论内容')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    username = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='评论用户')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='文章')

    class Meta:
        db_table = 'comment'
        verbose_name = '评论'
        verbose_name_plural = '所有评论'

    def __str__(self):
        return self.title


class Links(models.Model):
    title = models.CharField(max_length=30, verbose_name='链接标题')
    desc = models.CharField(max_length=50, verbose_name='链接描述')
    url = models.URLField(verbose_name='URL链接')
    date = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    index = models.IntegerField(default=0, verbose_name='排序顺序')

    class Meta:
        db_table = 'link'
        verbose_name = '友情链接'
        verbose_name_plural = '所有友情链接'
        ordering = ['index', 'id']

    def __str__(self):
        return self.title


class Advert(models.Model):
    title = models.CharField(max_length=30, verbose_name='链接标题')
    desc = models.CharField(max_length=50, verbose_name='链接描述')
    img = models.ImageField(upload_to='advert/%Y/%m/%d')
    url = models.URLField(verbose_name='URL链接')
    date = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    index = models.IntegerField(default=0, verbose_name='排序顺序')

    class Meta:
        db_table = 'advert'
        verbose_name = '广告'
        verbose_name_plural = '所有广告'
        ordering = ['index', 'id']

    def __str__(self):
        return self.title
