# news/admin.py
from django.contrib import admin
from .models import Category, Tag, Article,Subscribe
from modeltranslation.admin import TabbedTranslationAdmin

@admin.register(Article)
class ArticleAdmin(TabbedTranslationAdmin):
    list_display        = ('title', 'author', 'category')
    list_filter         = ('status', 'category', 'created_at')
    search_fields       = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}


    def publish_articles(self, request, queryset):
        queryset.update(status='published')
        list_filter=("status",)
    publish_articles.short_description = "Tanlanganllarni nashr et"

@admin.register(Category)
class CategoryAdmin(TabbedTranslationAdmin):
    list_filter=("name",)
    list_display        = ('name',)
    search_fields =("name",)

@admin.register(Tag)
class TagAdmin(TabbedTranslationAdmin):
    list_display        = ('name',)
    list_filter = ("name",)
    search_fields = ("name",)

@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display=("email",)

