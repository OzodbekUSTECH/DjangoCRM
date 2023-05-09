from django.contrib import admin
from django.urls import path, include, re_path
from API.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('api/v1/', include('API.urls')),
]
