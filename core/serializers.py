from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from core.models import Address, User, Profile, EmergencyContact
from .models import validate_snils, validate_passport

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

class ProfileSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    passport = serializers.CharField(required=False, validators=[validate_passport])
    snils = serializers.CharField(required=False, validators=[validate_snils])

    class Meta:
        model = Profile
        fields = ["id", "passport", "snils", "blood_type", "insurance", "address"]

    def create(self, validated_data):
        address_data = validated_data.pop("address", None)
        if address_data:
            try:
                address_serializer = AddressSerializer(data=address_data)
                address_serializer.is_valid(raise_exception=True)
                new_address = address_serializer.save()
            except ValidationError as e:
                raise serializers.ValidationError({"address": str(e)})
        try:
            profile = Profile.objects.create(address=new_address, **validated_data)
        except ValidationError as e:
            raise serializers.ValidationError({"profile": str(e)})
        return profile

    def update(self, instance, validated_data):
        address_data = validated_data.pop("address", None)
        if address_data:
            try:
                address_serializer = AddressSerializer(instance=instance.address,
                                                       data=address_data,
                                                       partial=True)
                address_serializer.is_valid(raise_exception=True)
                address_serializer.save()
            except ValidationError as e:
                raise serializers.ValidationError({"address": str(e)})

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    username = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "patronymic", "email", "is_test", "profile"]

    def create(self, validated_data):
        profile_data = validated_data.pop("profile", None)
        if profile_data:
            try:
                profile_serializer = ProfileSerializer(data=profile_data)
                profile_serializer.is_valid(raise_exception=True)
                profile = profile_serializer.save()
            except ValidationError as e:
                raise serializers.ValidationError({"profile": str(e)})
        try:
            print(validated_data)
            user = User.objects.create(profile=profile, **validated_data)
        except ValidationError as e:
            raise serializers.ValidationError({"user": str(e)})
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop("profile", None)
        if profile_data:
            try:
                profile_serializer = ProfileSerializer(instance=instance.profile,
                                                       data=profile_data,
                                                       partial=True)
                profile_serializer.is_valid(raise_exception=True)
                profile_serializer.save()
            except ValidationError as e:
                raise serializers.ValidationError({"profile": str(e)})

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

class EmergencySerializer(serializers.ModelSerializer):
    user = UserSerializer()

    def create(self, validated_data):
        user_data = validated_data.pop("user", None)
        if user_data:
            try:
                user_serializer = UserSerializer(data=user_data)
                user_serializer.is_valid(raise_exception=True)
                user = user_serializer.save()
            except ValidationError as e:
                raise serializers.ValidationError({"user": str(e)})

        try:
            emergency_contact = EmergencyContact.objects.create(user=user, **validated_data)
        except ValidationError as e:
            raise serializers.ValidationError({"emergency_contact": str(e)})

        return emergency_contact

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user", None)
        if user_data:
            try:
                user_serializer = UserSerializer(instance=instance.user,
                                                 data=user_data,
                                                 partial=True)
                user_serializer.is_valid(raise_exception=True)
                user_serializer.save()
            except ValidationError as e:
                raise serializers.ValidationError({"user": str(e)})

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

    class Meta:
        model = EmergencyContact
        fields = ["id", "name", "relation", "phone", "user"]