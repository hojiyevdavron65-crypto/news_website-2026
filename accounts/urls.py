from django.urls import path
from .views import signin_view,signup_view,logout_view,profile_page
urlpatterns=[
    path('login/',signin_view,name="login"),
    path("register/",signup_view,name="register"),
    path("logout",logout_view,name="logout"),
    path("profile/<int:pk>/",profile_page,name="profile"),
]