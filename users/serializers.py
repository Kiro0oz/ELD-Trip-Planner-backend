from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    phone = serializers.CharField(max_length=15, required=True, write_only=True)
    license_number = serializers.CharField(max_length=20, required=True, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password', 'phone', 'license_number']

    def validate_username(self, value):
        """Ensure username is unique"""
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("This username is already taken.")
        return value

    def validate_email(self, value):
        """Ensure email is unique"""
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already registered.")
        return value

    def validate_phone(self, value):
        """Ensure phone number is unique"""
        if Profile.objects.filter(phone=value).exists():
            raise serializers.ValidationError("This phone number is already in use.")
        return value

    def validate_license_number(self, value):
        """Ensure license number is unique"""
        if Profile.objects.filter(license_number=value).exists():
            raise serializers.ValidationError("This license number is already in use.")
        return value

    def create(self, validated_data):
        phone = validated_data.pop("phone")
        license_number = validated_data.pop("license_number")

        user = User.objects.create_user(**validated_data)

        Profile.objects.create(user=user, phone=phone, license_number=license_number)

        return user



class UserSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(source="profile.phone", read_only=True)
    license_number = serializers.CharField(source="profile.license_number", read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'phone', 'license_number']
