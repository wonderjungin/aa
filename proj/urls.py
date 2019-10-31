
from django.contrib import admin
from django.urls import path, include
from aa import urls
from rest_framework import urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aa.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
