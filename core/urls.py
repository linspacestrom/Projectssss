from django.urls import path, include
from rest_framework import routers

from core.views import AddressViewSet

router = routers.DefaultRouter()
router.register(r'address', AddressViewSet, basename='address')
urlpatterns = [
    path("", include(router.urls))
]