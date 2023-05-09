from django.urls import path, include
from rest_framework import routers
from .views import RecordViewSet

router = routers.DefaultRouter()

router.register('Users', RecordViewSet)

