from rest_framework import viewsets
from core.filters import UserFilter, ProfileFilter, AddressFilter, EmergencyContactFilter
from core.models import Address, User, Profile, EmergencyContact
from core.serializers import AddressSerializer, UserSerializer, ProfileSerializer, EmergencySerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    filterset_class = AddressFilter

    @extend_schema(
        summary='Update an existing address',
        description='This endpoint allows you to update an existing address by its ID.',
        request=AddressSerializer,
        responses={200: AddressSerializer},
        tags=['Addresses'],
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

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

    @extend_schema(
        summary="Получить список пользователей",
        description="Возвращает список пользователей",
        parameters=[
            OpenApiParameter(name="username", description="Фильтр по юзернйему", required=True, type=str),
            OpenApiParameter(name="first_name", description="Фильтр по имени", required=True, type=str),
            OpenApiParameter(name="last_name", description="Фильтр по фамилии", required=True, type=str),
            OpenApiParameter(name="patronymic", description="Фильтр по отчество", required=True, type=str),
            OpenApiParameter(name="email", description="Фильтр по электронной почте", required=True, type=str),
            OpenApiParameter(name="is_test", description="Фильтр по роле разработчика", required=True, type=bool),
            OpenApiParameter(name="profile", description="Идентификатор пользователя", required=True, type=int)
        ],
        responses={
            200: AddressSerializer,
            400: OpenApiResponse(description="Ошибка валидации данных"),
            404: OpenApiResponse(description="Пользователь не найден")
        },
        tags=["Пользователи"],
        operation_id="listUsers",
        deprecated=False,
    )
    def list(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

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