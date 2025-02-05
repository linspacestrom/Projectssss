# Generated by Django 5.1.5 on 2025-02-03 12:53

import core.models
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(choices=[('Москва', 'Москва'), ('Санкт-Петербург', 'Санкт-Петербург'), ('Краснодарский край', 'Краснодарский край'), ('Свердловская область', 'Свердловская область'), ('Тульская область', 'Тульская область'), ('Нижегородская область', 'Нижегородская область'), ('Челябинская область', 'Челябинская область'), ('Калининградская область', 'Калининградская область'), ('Республика Татарстан', 'Республика Татарстан'), ('Республика Башкортостан', 'Республика Башкортостан')], max_length=80, verbose_name='Регион')),
                ('city', models.CharField(max_length=80, verbose_name='Город')),
                ('area', models.CharField(max_length=80, verbose_name='Район')),
                ('street', models.CharField(max_length=80, verbose_name='Улица')),
                ('house_number', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Номер дома')),
                ('entrance', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Подьезд')),
                ('floor', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)], verbose_name='Этаж')),
                ('apartment_number', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10000)], verbose_name='Номер квартиры')),
                ('coordinates_x', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(-180.0), django.core.validators.MaxValueValidator(180.0)], verbose_name='Долгота')),
                ('coordinates_y', models.DecimalField(decimal_places=2, max_digits=4, validators=[django.core.validators.MinValueValidator(-90.0), django.core.validators.MaxValueValidator(90.0)], verbose_name='Широта')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passport', models.CharField(max_length=10, unique=True, validators=[core.models.validate_passport], verbose_name='Паспорт')),
                ('snils', models.CharField(max_length=11, unique=True, validators=[core.models.validate_snils], verbose_name='Снилс')),
                ('blood_type', models.CharField(choices=[('1 отрицательная группа крови ', 'O-'), ('1 положительная группа крови', 'O+'), ('2 отрицательная группа крови', 'A-'), ('2 положительная группа крови', 'A+'), ('3 отрицательная группа крови', 'B-'), ('3 положительная группа крови', 'B+'), ('4 отрицатлеьная группа крови', 'AB-'), ('4 положительная группа крови', 'AB+')], max_length=30, verbose_name='Группа крови')),
                ('insurance', models.CharField(max_length=16, validators=[core.models.validate_insurance], verbose_name='Номер страхового полиса')),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile_address', to='core.address', verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('patronymic', models.CharField(default='Отсутствует', max_length=120, verbose_name='Отчество')),
                ('is_test', models.BooleanField(default=False, verbose_name='Тестировщик')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='custom_user_set', to='auth.group', verbose_name='groups')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_abstract_profile', to='core.profile', verbose_name='Профиль')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='custom_user_permissions_set', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='EmergencyContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Имя')),
                ('relation', models.CharField(choices=[('Друзья', 'Друзья'), ('Родственники', 'Родственники'), ('Жена/Девушка', 'Жена/Девушка'), ('Муж/Парень', 'Муж/Парень'), ('Мама', 'Мама'), ('Папа', 'Папа'), ('Брат', 'Брат'), ('Сестра', 'Сестра'), ('Бабушка', 'Бабушка'), ('Дедушка', 'Дедушка'), ('Дочь', 'Дочь'), ('Сын', 'Сын')], max_length=100, verbose_name='Отношение')),
                ('phone', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='Неверно введен номер телефона', regex='^\\+?[78]{1}9\\d{9}$')], verbose_name=' Номер телефона')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='emergency_user_contact', to='core.user')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
    ]
