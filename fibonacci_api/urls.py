from django.urls import include, path
from rest_framework import routers

from .views import NumberRequestedViewSet


router = routers.DefaultRouter()
router.register('fibonacci', NumberRequestedViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
