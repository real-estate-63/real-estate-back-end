from abc import ABC

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from allauth.utils import email_address_exists
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from allauth.account import app_settings as allauth_settings

from systems.models import Country, ProvinceCity, District, Ward
from users.models import User


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


class RegisterSerializer(serializers.Serializer):
    # Account
    username = serializers.CharField(required=True, max_length=254, write_only=True)
    email = serializers.EmailField(required=True, max_length=254)
    user_type = serializers.CharField(required=True, max_length=10)
    # Profile
    first_name = serializers.CharField(required=True, max_length=30, write_only=True)
    middle_name = serializers.CharField(required=True, max_length=150, write_only=True)
    last_name = serializers.CharField(required=True, max_length=150, write_only=True)
    password1 = serializers.CharField(required=True, max_length=128, write_only=True)
    password2 = serializers.CharField(required=True, max_length=128, write_only=True)

    phone_number = serializers.CharField(required=True, max_length=14, write_only=True)
    birth_date = serializers.DateField(required=True, write_only=True, format="%Y/%m/%d",
                                       input_formats=["%Y/%m/%d"])
    # Address
    country = serializers.CharField(required=True, max_length=14, write_only=True)
    province_city = serializers.CharField(required=True, max_length=14, write_only=True)
    district = serializers.CharField(required=True, max_length=14, write_only=True)
    ward = serializers.CharField(required=True, max_length=14, write_only=True)
    name_street = serializers.CharField(required=True, max_length=254, write_only=True)
    number = serializers.CharField(required=True, max_length=14, write_only=True)
    adress = serializers.IntegerField(read_only=True)

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    _("A user is already registered with this e-mail address.")
                )
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(_("The two password fields didn't match."))
        return data

    def get_cleaned_data(self):
        return {
            'email':
                self.validated_data.get('email', ''),
            'password1':
                self.validated_data.get('password1', ''),
            'user_type':
                self.validated_data.get('user_type', ''),
            'first_name':
                self.validated_data.get('first_name', ''),
            'middle_name':
                self.validated_data.get('middle_name', ''),
            'last_name':
                self.validated_data.get('last_name', ''),
            'address':
                self.validated_data.get('address', ''),
            'phone_number':
                self.validated_data.get('phone_number', ''),
            'birth_date':
                self.validated_data.get('birth_date', ''),
            'country':
                self.validated_data.get('country', ''),
            'province_city':
                self.validated_data.get('province_city', ''),
            'district':
                self.validated_data.get('district', ''),
            'ward':
                self.validated_data.get('ward', ''),
            'name_street':
                self.validated_data.get('name_street', ''),
            'number':
                self.validated_data.get('number', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        user.clinic_id = 1
        user.save()
        return user


# Address

class GetCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name', 'code')


class GetProvinceCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProvinceCity
        fields = ('id', 'name', 'code')


class GetDistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ('id', 'name', 'code')


class GetWardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = ('id', 'name', 'code')
