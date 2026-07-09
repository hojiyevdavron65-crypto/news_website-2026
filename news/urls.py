from django.urls import path
from .views import home_page,single_page_view,sport_view,local_view,global_view,techno_view,society_view,finance_view,edu_view

urlpatterns=[
    path('',home_page,name="home"),
    path("new/<slug:slug>/",single_page_view,name="single"),
    path("sport/",sport_view,name="sport"),
    path("local/",local_view,name="local"),
    path("global/",global_view,name="global"),
    path("society/",society_view,name="society"),
    path("techno/",techno_view,name="techno"),
    path("edu/",edu_view,name="edu"),
    path("finance/",finance_view,name="finance"),
]