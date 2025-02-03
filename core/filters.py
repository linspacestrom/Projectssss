from django_filters.rest_framework import FilterSet
from .models import User


class UserFilter(FilterSet):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email"]