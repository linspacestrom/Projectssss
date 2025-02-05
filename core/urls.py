from django.urls import path, include
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from core.views import AddressViewSet, UserViewSet, ProfileViewSet, EmergencyContactViewSet

routers = routers.DefaultRouter()
routers.register('users', UserViewSet)
routers.register("profiles", ProfileViewSet)
routers.register('addresses', AddressViewSet)
routers.register('emergencies', EmergencyContactViewSet)
print(routers.urls)
urlpatterns = [path("api/schema", SpectacularAPIView.as_view(), name="schema"),
               path("api/docs", SpectacularSwaggerView.as_view(), name="swagger")]

urlpatterns += routers.urls