from django.contrib import admin
from .models import User,Profile
# Register your models here.
@admin.register(User)
class User(admin.ModelAdmin):
    list_display=("username","email")
    search_fields=("username",)

@admin.register(Profile)
class Profile(admin.ModelAdmin):
    list_display=("user",)


