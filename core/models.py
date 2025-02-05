from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.db import models
from core.consts import TYPE_BLOOD, REGION, TYPE_RELATION
import re

def validate_passport(passport):
    if re.search(r"^[0-9]{10}$", passport) is None:
        raise ValidationError("Паспорт должен содержать 10 цифр")

def validate_snils(snils):
    if re.search(r"^[0-9]{11}$", snils) is None:
        raise ValidationError("Снилс должен содержать 11 цифр")

def validate_number_phone_one(phone):
    if re.search(r"^\+?[78]\(9\d{2}\)\d{7}$", phone) is None:
        raise ValidationError("Неверно введен номер телефона")

def validate_number_phone_two(phone):
    if re.search(r"^\+?[78]9\d{9}$", phone) is None:
        raise ValidationError("Неверно введен номер телефона")

def validate_insurance(insurance):
    if re.search(r"^[0-9]{16}$", insurance) is None:
        raise ValidationError("Неверно введен страховой полис")

class User(AbstractUser):
        patronymic = models.CharField(max_length=120, verbose_name="отчество", default="Отсутствует")
        profile = models.OneToOneField("Profile",
                                       on_delete=models.CASCADE,
                                       related_name="user_abstract_profile",
                                       verbose_name="профиль")
        is_test = models.BooleanField(default=False, verbose_name="тестировщик")
        groups = models.ManyToManyField(
            Group,
            related_name='custom_user_set',
            blank=True,
            help_text='The groups this user belonnstance.get("passport", validated_data["passport"])gs to. A user will get all permissions '
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
    passport = models.CharField(max_length=10, verbose_name="паспорт", unique=True,
                                validators=[validate_passport])
    snils = models.CharField(max_length=11, verbose_name="cнилс", unique=True,
                             validators=[validate_snils])
    blood_type = models.CharField(max_length=30, verbose_name="группа крови", choices=TYPE_BLOOD)
    insurance = models.CharField(max_length=16, verbose_name="номер страхового полиса", validators=[validate_insurance])
    address = models.OneToOneField("Address",
                                   on_delete=models.CASCADE,
                                   related_name="profile_address",
                                   verbose_name="адрес")

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self):
        return f"{self.passport} {self.snils}"

class Address(models.Model):
    region = models.CharField("регион", max_length=80, choices=REGION)
    city = models.CharField("город", max_length=80)
    area = models.CharField("район", max_length=80)
    street = models.CharField("улица", max_length=80)
    house_number = models.PositiveSmallIntegerField("номер дома", validators=[MinValueValidator(1)])
    entrance = models.PositiveSmallIntegerField("подьезд", validators=[MinValueValidator(1), MaxValueValidator(100)])
    floor = models.PositiveSmallIntegerField("этаж", validators=[MinValueValidator(1), MaxValueValidator(1000)])
    apartment_number = models.PositiveSmallIntegerField("номер квартиры", validators=[MinValueValidator(1), MaxValueValidator(10000)])
    coordinates_x = models.DecimalField("долгота", max_digits=5, decimal_places=2, validators=[MinValueValidator(-180.00), MaxValueValidator(180.00)] )
    coordinates_y = models.DecimalField("широта",max_digits=4, decimal_places=2, validators=[MinValueValidator(-90.00), MaxValueValidator(90.00)])

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"

    def __str__(self):
        return f"{self.street} {self.house_number} {self.city}"

class EmergencyContact(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="emergency_user_contact")
    name = models.CharField(max_length=80, verbose_name="имя")
    relation = models.CharField(max_length=100, verbose_name="отношение", choices=TYPE_RELATION)
    phone = models.CharField(max_length=100, verbose_name=" номер телефона", validators=[RegexValidator(
        regex=r"^\+?[78]{1}9\d{9}$",
        message="Неверно введен номер телефона"
    )])

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return f"{self.name} приходится {self.user.first_name} {self.user.last_name} {self.relation}"