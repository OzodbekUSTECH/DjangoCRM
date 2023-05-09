from django.contrib import admin
from django.urls import path, include
from API.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('api/v1/', include(router.urls))
]
