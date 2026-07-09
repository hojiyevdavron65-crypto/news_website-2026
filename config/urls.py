from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admindavron/', admin.site.urls),
    path("",include("news.urls")),
    path("interaction/",include("interactions.urls")),
    path("account/",include("accounts.urls")),
    path('i18n',include('django.conf.urls.i18n')),# til almashtirish

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

