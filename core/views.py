from django.shortcuts import render
from rest_framework import viewsets
from core.models import Address
from core.serializers import AddressSerializer
# Create your views here.


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer