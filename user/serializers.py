from rest_framework import serializers

from user.models import User


class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class UserSignInSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('comparative_name', 'password')
        extra_kwargs = {"username": {"write_only": True}}
