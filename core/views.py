from django.shortcuts import render
from rest_framework import viewsets, generics
from core.models import Address, User, Profile, EmergencyContact
from core.serializers import AddressSerializer, UserSerializer, ProfileSerializer, EmergencySerializer
# Create your views here.


class AddressRetrieveUpdateViewSet(generics.RetrieveUpdateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class AddressListCreateViewSet(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class AddressRetrieveDestroyViewSet(generics.RetrieveDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class ProfileRetrieveDestroyViewSet(generics.RetrieveDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileListCreateViewSet(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class UserRetrieveDestroyViewSet(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserListCreateViewSet(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateViewSet(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EmergencyContactListCreateViewSet(generics.ListCreateAPIView):
    queryset = EmergencyContact.objects.all()
    serializer_class = EmergencySerializer

class EmergencyContactRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = EmergencyContact.objects.all()
    serializer_class = EmergencySerializer

class EmergencyContactRetrieveDestroyViewSet(generics.RetrieveDestroyAPIView):
    queryset = EmergencyContact.objects.all()
    serializer_class = EmergencySerializer