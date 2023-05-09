from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from website.models import Record
from .serializers import RecordSerializer

class RecordViewSet(ModelViewSet):
    queryset = Record.objects.order_by('id')
    serializer_class = RecordSerializer