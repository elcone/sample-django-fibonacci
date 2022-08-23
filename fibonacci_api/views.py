from rest_framework import viewsets

from .models import NumberRequested
from .serializers import NumberRequestedSerializer


class NumberRequestedViewSet(viewsets.ModelViewSet):
    queryset = NumberRequested.objects.all()
    serializer_class = NumberRequestedSerializer
