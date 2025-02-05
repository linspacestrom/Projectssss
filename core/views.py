from rest_framework import viewsets
from core.filters import UserFilter, ProfileFilter, AddressFilter, EmergencyContactFilter
from core.models import Address, User, Profile, EmergencyContact
from core.serializers import AddressSerializer, UserSerializer, ProfileSerializer, EmergencySerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    filterset_class = AddressFilter

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filterset_class = ProfileFilter
class EmergencyContactViewSet(viewsets.ModelViewSet):
    queryset = EmergencyContact.objects.all()
    serializer_class = EmergencySerializer
    filterset_class = EmergencyContactFilter

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilter

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