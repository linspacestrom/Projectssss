from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter

from core.filters import UserFilter, ProfileFilter, AddressFilter, EmergencyContactFilter
from core.models import Address, User, Profile, EmergencyContact
from core.pagination import UserPageNumberPagination, ProfilePageNumberPagination, AddressPageNumberPagination, \
    EmergencyPageNumberPagination
from core.serializers import AddressSerializer, UserSerializer, ProfileSerializer, EmergencySerializer
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_class = AddressFilter
    search_fields = ("passport", "snils", "insurance")
    pagination_class = AddressPageNumberPagination

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_class = ProfileFilter
    search_fields = ("passport", "snils", "insurance")
    pagination_class = ProfilePageNumberPagination

class EmergencyContactViewSet(viewsets.ModelViewSet):
    queryset = EmergencyContact.objects.all()
    serializer_class = EmergencySerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_class = EmergencyContactFilter
    search_fields = ("name", "relation", "phone")
    pagination_class = EmergencyPageNumberPagination

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_class = UserFilter
    search_fields = ("first_name", "last_name", "patronymic", "email")
    pagination_class = UserPageNumberPagination

# class AddressRetrieveUpdateViewSet(generics.RetrieveUpdateAPIView):
#     queryset = Address.objects.all()
#     serializer_class = AddressSerializer
#
# class AddressListCreateViewSet(generics.ListCreateAPIView):
#     queryset = Address.objects.all()
#     serializer_class = AddressSerializer
#
# class AddressRetrieveDestroyViewSet(generics.RetrieveDestroyAPIView):
#     queryset = Address.objects.all()
#     serializer_class = AddressSerializer
#
# class ProfileRetrieveDestroyViewSet(generics.RetrieveDestroyAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#
# class ProfileListCreateViewSet(generics.ListCreateAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#
# class ProfileRetrieveUpdate(generics.RetrieveUpdateAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#
# class UserRetrieveDestroyViewSet(generics.RetrieveDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
# class UserListCreateViewSet(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     filter_backends = (DjangoFilterBackend,)
#     filter_class = UserFilter
#
# class UserRetrieveUpdateViewSet(generics.RetrieveUpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
# class EmergencyContactListCreateViewSet(generics.ListCreateAPIView):
#     queryset = EmergencyContact.objects.all()
#     serializer_class = EmergencySerializer
#
# class EmergencyContactRetrieveUpdate(generics.RetrieveUpdateAPIView):
#     queryset = EmergencyContact.objects.all()
#     serializer_class = EmergencySerializer
#
# class EmergencyContactRetrieveDestroyViewSet(generics.RetrieveDestroyAPIView):
#     queryset = EmergencyContact.objects.all()
#     serializer_class = EmergencySerializer