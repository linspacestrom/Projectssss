from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.db import models
from core.consts import TYPE_BLOOD, REGION, TYPE_RELATION
from core.validators import validate_snils, validate_passport, validate_insurance
class User(AbstractUser):
        patronymic = models.CharField("отчество", max_length=120, default="Отсутствует")
        profile = models.OneToOneField("Profile",
                                       on_delete=models.CASCADE,
                                       related_name="user_abstract_profile",
                                       verbose_name="профиль")
        is_test = models.BooleanField("тестировщик", default=False,)
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
    passport = models.CharField("паспорт", max_length=10, unique=True,
                                validators=[validate_passport])
    snils = models.CharField("cнилс", max_length=11, unique=True,
                             validators=[validate_snils])
    blood_type = models.CharField("группа крови", max_length=30, choices=TYPE_BLOOD)
    insurance = models.CharField("номер страхового полиса", max_length=16, validators=[validate_insurance])
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
    name = models.CharField("имя", max_length=80)
    relation = models.CharField("отношение", max_length=100, choices=TYPE_RELATION)
    phone = models.CharField("номер телефона", max_length=100, validators=[RegexValidator(
        regex=r"^\+?[78]{1}9\d{9}$",
        message="Неверно введен номер телефона"
    )])

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return f"{self.name} приходится {self.user.first_name} {self.user.last_name} {self.relation}"