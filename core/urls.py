from django.urls import path, include
from rest_framework import routers

from core.models import EmergencyContact
from core.views import ProfileListCreateViewSet, ProfileRetrieveUpdate, ProfileRetrieveDestroyViewSet, \
    AddressListCreateViewSet, \
    AddressRetrieveDestroyViewSet, AddressRetrieveUpdateViewSet, UserListCreateViewSet, UserRetrieveUpdateViewSet, \
    EmergencyContactListCreateViewSet, EmergencyContactRetrieveUpdate, EmergencyContactRetrieveDestroyViewSet

urlpatterns = [
    path("backend/api/v1/profile/", ProfileListCreateViewSet.as_view()),
    path("backend/api/v1/profile/<int:pk>/", ProfileRetrieveUpdate.as_view()),
    path("backend/api/v1/profiledelete/<int:pk>/", ProfileRetrieveDestroyViewSet.as_view()),
    path("backend/api/v1/address/", AddressListCreateViewSet.as_view()),
    path("backend/api/v1/address/<int:pk>/", AddressRetrieveUpdateViewSet.as_view()),
    path("backend/api/v1/addressdelete/<int:pk>/", AddressRetrieveDestroyViewSet.as_view()),
    path("backend/api/v1/address/", AddressRetrieveUpdateViewSet.as_view()),
    path("backend/api/v1/users/", UserListCreateViewSet.as_view()),
    path("backend/api/v1/users/<int:pk>/", UserRetrieveUpdateViewSet.as_view()),
    path("backend/api/v1/usersdelete/<int:pk>", UserRetrieveUpdateViewSet.as_view()),
    path("backend/api/v1/contacts/", EmergencyContactListCreateViewSet.as_view()),
    path("backend/api/v1/contacts/<int:pk>/", EmergencyContactRetrieveUpdate.as_view()),
    path("backend/api/v1/contactsdelete/<int:pk>/", EmergencyContactRetrieveDestroyViewSet.as_view())
]