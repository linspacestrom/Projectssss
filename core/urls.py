from django.urls import path, include
from rest_framework import routers
from core.views import AddressViewSet, UserViewSet, ProfileViewSet, EmergencyContactViewSet

routers = routers.DefaultRouter()
routers.register('users', UserViewSet)
routers.register("profiles", ProfileViewSet)
routers.register('addresses', AddressViewSet)
routers.register('emergencies', EmergencyContactViewSet)
urlpatterns = []

urlpatterns += routers.urls