from django_filters.rest_framework import FilterSet
from django_filters.rest_framework import filters
from .models import User, TYPE_RELATION, TYPE_BLOOD, Profile, REGION, Address, EmergencyContact


class UserFilter(FilterSet):
    name = filters.CharFilter('first_name', lookup_expr='iexact')
    surname = filters.CharFilter('last_name', lookup_expr='exact')
    patronymic = filters.CharFilter('patronymic', lookup_expr='exact')
    email = filters.CharFilter('email', lookup_expr='icontains', label="Почтовый адрес")
    is_test = filters.BooleanFilter('is_test', lookup_expr='exact', label="Пользователь-тестировщик")
    name_emergency_contact = filters.CharFilter('emergency_user_contact__name', lookup_expr='icontains', label='Имя экстренного контакта')
    relation = filters.ChoiceFilter(field_name='emergency_user_contact__relation', choices=TYPE_RELATION, label='Отношение')
    phone_emergency_contact = filters.CharFilter(field_name="phone", lookup_expr="icontains", label="Номер экстренного контакта")

    class Meta:
        model = User
        fields = ["name", "surname", "patronymic", "email", "is_test", "name_emergency_contact", "relation", "phone_emergency_contact"]

class ProfileFilter(FilterSet):
    passport = filters.CharFilter("passport", lookup_expr='iexact', label="Паспорт")
    snils = filters.CharFilter("snils", lookup_expr='iexact', label="Снилс")
    insurance = filters.CharFilter("insurance", "iexact", label="Номер страхового полиса")
    blood_type = filters.ChoiceFilter("blood_type", choices=TYPE_BLOOD, label="Группа крови")
    user_name = filters.CharFilter('user_abstract_profile__first_name', lookup_expr='iexact', label="Имя")
    user_surname = filters.CharFilter('user_abstract_profile__last_name', lookup_expr='exact', label="Фамилия")
    user_patronymic = filters.CharFilter('user_abstract_profile__patronymic', lookup_expr='exact', label="Отчество")
    user_email = filters.CharFilter('user_abstract_profile__email', lookup_expr='icontains', label="Почтовый адрес")
    user_is_test = filters.BooleanFilter('user_abstract_profile__is_test', lookup_expr='exact', label="Тестировщик")

    class Meta:
        model = Profile
        fields = ["passport", "snils", "insurance",
                  "blood_type", "user_name", "user_surname",
                  "user_patronymic", "user_is_test"]

class AddressFilter(FilterSet):
    region = filters.ChoiceFilter("region", choices = REGION, label="Регион")
    city = filters.CharFilter("city", lookup_expr="exact", label="Город")
    area = filters.CharFilter("area", lookup_expr="iexact", label="Район")
    street = filters.CharFilter("street", lookup_expr="iexact", label="Улица")
    house_number = filters.RangeFilter("house_number", lookup_expr="range", label="Номер дома")
    entrance = filters.RangeFilter("entrance", lookup_expr="range", label="Номер подъезда")
    floor = filters.RangeFilter("floor", lookup_expr="range", label="Этаж")
    apartment_number = filters.RangeFilter("apartment_number", lookup_expr="range", label="Номер квартиры")
    coordinates_x = filters.RangeFilter("coordinates_x", lookup_expr="range", label="Координаты долготы")
    coordinates_y = filters.RangeFilter("coordinates_y", lookup_expr="range", label="Координаты широты")

    class Meta:
        model = Address
        fields = ["region", "city", "area",
                  "street", "house_number", "entrance",
                  "floor", "apartment_number", "coordinates_x",
                  "coordinates_y"]

class EmergencyContactFilter(FilterSet):
    name = filters.CharFilter("name", lookup_expr="iexact", label="Имя экстренного контакта")
    relation = filters.ChoiceFilter(field_name="relation", choices=TYPE_RELATION, label="Тип взаимоотношений")
    phone = filters.CharFilter("phone", lookup_expr="contains", label="Номер телефона экстренного контакта")
    user_name = filters.CharFilter('user__first_name', lookup_expr='iexact', label="Имя пользователя")
    user_surname = filters.CharFilter('user__last_name', lookup_expr='exact', label="Фамилия пользователя")
    user_patronymic = filters.CharFilter('user__patronymic', lookup_expr='exact', label="Отчество пользователя")
    user_email = filters.CharFilter('user__email', lookup_expr='icontains', label="Почтовый адрес")
    user_is_test = filters.BooleanFilter('user__is_test', lookup_expr='exact', label="Пользователь-тестирощик")