from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxLengthValidator, MaxValueValidator, RegexValidator
from django.db import models
from django.contrib.gis.db import models as geomodels
import re

# Create your models here.

TYPE_BLOOD = [
    ("1 отрицательная группа крови ", "O-"),
    ("1 положительная группа крови", 'O+'),
    ("2 отрицательная группа крови", "A-"),
    ("2 положительная группа крови", "A+"),
    ("3 отрицательная группа крови", "B-"),
    ("3 положительная группа крови", "B+"),
    ("4 отрицатлеьная группа крови", "AB-"),
    ("4 положительная группа крови", "AB+")
]

TYPE_RELATION = [
    ("Друзья", "Друзья"),
    ("Родственники", "Родственники"),
    ("Жена/Девушка", "Жена/Девушка"),
    ("Муж/Парень", "Муж/Парень"),
    ("Мама", "Мама"),
    ("Папа", "Папа"),
    ("Брат", "Брат"),
    ("Сестра", "Сестра"),
    ("Бабушка", "Бабушка"),
    ("Дедушка", "Дедушка"),
    ("Дочь", "Дочь"),
    ("Сын", "Сын")
]

REGION = [
    ("Москва", "Москва"),
    ("Санкт-Петербург", "Санкт-Петербург"),
    ("Краснодарский край", "Краснодарский край"),
    ("Свердловская область", "Свердловская область"),
    ("Тульская область", "Тульская область"),
    ("Нижегородская область", "Нижегородская область"),
    ("Челябинская область", "Челябинская область"),
    ("Калининградская область", "Калининградская область"),
    ("Республика Татарстан", "Республика Татарстан"),
    ("Республика Башкортостан", "Республика Башкортостан")
]

def validate_passport(passport):
    if re.search(r"^[0-9]{10}$", passport) is None:
        raise ValidationError("Паспорт должен содержать 10 цифр")

def validate_snils(snils):
    if re.search(r"^[0-9]{11}$", snils) is None:
        raise ValidationError("Снилс должен содержать 11 цифр")


def validate_number_phone_one(phone):
    if re.search(r"^\+{0,1}[78]\(9\d{2}\)\d{7}$", phone) is None:
        raise ValidationError("Неверно введен номер телефона")

def validate_number_phone_two(phone):
    if re.search(r"^\+?[78]9\d{9}$", phone) is None:
        raise ValidationError("Неверно введен номер телефона")

def validate_insurance(insurance):
    if re.search(r"^[0-9]{16}$", insurance) is None:
        raise ValidationError("Неверно введен страховой полис")

class User(AbstractUser):
        patronymic = models.CharField(max_length=120, verbose_name="Отчество", default="Отсутствует")
        profile = models.OneToOneField("Profile",
                                       on_delete=models.CASCADE,
                                       related_name="user_abstract_profile",
                                       verbose_name="Профиль")
        is_test = models.BooleanField(default=False, verbose_name="Тестировщик")
        groups = models.ManyToManyField(
            Group,
            related_name='custom_user_set',
            blank=True,
            help_text='The groups this user belongs to. A user will get all permissions '
                      'granted to each of their groups.',
            verbose_name='groups'
        )

        user_permissions = models.ManyToManyField(
            Permission,
            related_name='custom_user_permissions_set',
            blank=True,
            help_text='Specific permissions for this user.',
            verbose_name='user permissions'
        )

        class Meta:
            verbose_name = "Пользователь"
            verbose_name_plural = "Пользователи"

        def __str__(self):
            return f"{self.first_name} {self.last_name}"

class Profile(models.Model):
    passport = models.CharField(max_length=10, verbose_name="Паспорт", unique=True,
                                validators=[validate_passport])
    snils = models.CharField(max_length=11, verbose_name="Снилс", unique=True,
                             validators=[validate_snils])
    blood_type = models.CharField(max_length=30, verbose_name="Группа крови", choices=TYPE_BLOOD)
    insurance = models.CharField(max_length=16, verbose_name="Номер страхового полиса", validators=[validate_insurance])
    address = models.OneToOneField("Address",
                                   on_delete=models.CASCADE,
                                   related_name="profile_address",
                                   verbose_name="Адрес")

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self):
        return f"{self.passport} {self.snils}"


class Address(models.Model):
    region = models.CharField("Регион", max_length=80, choices=REGION)
    city = models.CharField("Город", max_length=80)
    area = models.CharField("Район", max_length=80)
    street = models.CharField("Улица", max_length=80)
    house_number = models.PositiveSmallIntegerField("Номер дома", validators=[MinValueValidator(1)])
    entrance = models.PositiveSmallIntegerField("Подьезд", validators=[MinValueValidator(1), MaxValueValidator(100)])
    floor = models.PositiveSmallIntegerField("Этаж", validators=[MinValueValidator(1), MaxValueValidator(1000)])
    apartment_number = models.PositiveSmallIntegerField("Номер квартиры", validators=[MinValueValidator(1), MaxValueValidator(10000)])
    coordinates_x = models.DecimalField("Долгота", max_digits=5, decimal_places=2, validators=[MinValueValidator(-180.00), MaxValueValidator(180.00)] )
    coordinates_y = models.DecimalField("Широта",max_digits=4, decimal_places=2, validators=[MinValueValidator(-90.00), MaxValueValidator(90.00)])

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"

    def __str__(self):
        return f"{self.street} {self.house_number} {self.city}"

class EmergencyContact(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="emergency_user_contact")
    name = models.CharField(max_length=80, verbose_name="Имя")
    relation = models.CharField(max_length=100, verbose_name="Отношение", choices=TYPE_RELATION)
    phone = models.CharField(max_length=100, verbose_name=" Номер телефона", validators=[RegexValidator(
        regex=r"^\+?[78]{1}9\d{9}$",
        message="Неверно введен номер телефона"
    )])

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return f"{self.name} приходится {self.user.first_name} {self.user.last_name} {self.relation}"