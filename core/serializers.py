from rest_framework import serializers
from core.models import Address, User, Profile, EmergencyContact


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Profile
        fields = ["id", "passport", "snils", "blood_type", "insurance", "address"]


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "patronymic", "email", "is_test", "profile"]


class EmergencySerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = EmergencyContact
        fields = ["id", "name", "relation", "phone", "user"]