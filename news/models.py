from django.db import models
from django.utils.text import slugify
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Kategoriyalar'

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="published")

class Article(models.Model):
    STATUS=(('draft','Qoralama'),('published','Nashr etilgan'))

    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,blank=True)
    cover= models.ImageField(upload_to="articles/", blank=True, null=True)
    body= models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articles')
    category= models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='articles')
    tags = models.ManyToManyField(Tag, blank=True, related_name = 'articles')
    status= models.CharField(max_length=10, choices=STATUS, default='draft')
    views_count = models.PositiveIntegerField(default=0)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    objects=models.Manager()
    published=PublishedManager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        #O'zbek tilida
        if not self.slug_uz and self.title_uz:
            self.slug_uz = slugify(self.title_uz)
        #Ingliz tilida
        if not self.slug_en and self.title_en:
            self.slug_en = slugify(self.title_en)
        #Rus tilida
        if not self.slug_ru and self.title_ru:
            self.slug_ru = slugify(self.title_ru)

        super().save( *args, ** kwargs)

    def __str__(self):
          return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "YangilikLar"

class Subscribe(models.Model):
    email=models.EmailField()

    def __str__(self):
        return self.email
