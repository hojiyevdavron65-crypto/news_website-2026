from django.contrib import admin
from .models import Comment,Like,Contact
# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=("article","author",)
    list_filter=("created_at",)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display=("user","article")

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=("name",)
