from django.urls import path, include, re_path
from rest_framework import routers
from .views import RecordViewSet
# from djoser.views import UserViewSet

router = routers.DefaultRouter()
router.register('Users', RecordViewSet)

#нет смысла в этом, через админку можно смотреть Users
# router.register('Admin', UserViewSet)







urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
    #лучше не стоит этот путь делать, так как могут легко получить токен
    # re_path('getToken/', include('djoser.urls.authtoken'))
]
