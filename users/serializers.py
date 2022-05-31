from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from allauth.utils import email_address_exists
from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers, exceptions
from allauth.account import app_settings as allauth_settings

from realEstateBackEnd.settings import INSTALLED_APPS, ACCOUNT_AUTHENTICATION_METHOD
from systems.models import Country, ProvinceCity, District, Ward
from users.models import UserProfile, Address

UserModel = get_user_model()


# ################################################## ACCOUNT ##########################################################
class RegisterSerializer(serializers.Serializer):
    # Account
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
    address = serializers.IntegerField(read_only=True)

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


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False, allow_blank=True)
    password = serializers.CharField(style={'input_type': 'password'})

    def authenticate(self, **kwargs):
        return authenticate(self.context['request'], **kwargs)

    def _validate_email(self, email, password):
        user = None

        if email and password:
            try:
                user = self.authenticate(email=email, password=password)
                print(user)
            except Exception as e:
                print(e)
        else:
            msg = _('Must include "email" and "password".')
            raise exceptions.ValidationError(msg)

        return user

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = None

        if 'allauth' in INSTALLED_APPS:
            from allauth.account import app_settings
            if ACCOUNT_AUTHENTICATION_METHOD == app_settings.AuthenticationMethod.USERNAME_EMAIL:
                user = self._validate_email(email, password)

        # Did we get back an active user?
        if user:
            if not user.is_active:
                msg = _('User account is disabled.')
                raise exceptions.ValidationError(msg)
        else:
            msg = _('Unable to log in with provided credentials.')
            raise exceptions.ValidationError(msg)

        attrs['user'] = user
        return attrs


class ResendAuthEmailSerializer(serializers.Serializer):
    key = serializers.CharField()


# ################################################## ACCOUNT ##########################################################

# ################################################### USER ############################################################
class UserManagementAddressSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Address
        fields = ('id',
                  'country',
                  'province_city',
                  'district',
                  'ward',
                  'name_street',
                  'number')
        read_only_fields = ('id',)


class UserManagementProfileSerializer(serializers.ModelSerializer):
    address_profile = UserManagementAddressSerializer(many=True)

    class Meta:
        model = UserProfile
        fields = ('first_name',
                  'middle_name',
                  'last_name',
                  'phone_number',
                  'birth_date',
                  'address_profile')

    def get_address(self, obj):
        try:
            if Address.objects.filter(id=obj.address.id).exists() is True:
                get_address = Address.objects.get(id=obj.address.id)
                data = UserManagementAddressSerializer(get_address).data
                return data
            else:
                return {}
        except AttributeError:
            return {}

    def update(self, instance, validated_data):
        address_profile = validated_data.pop('address_profile')
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.middle_name = validated_data.get('middle_name', instance.middle_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.save()
        for add in address_profile:
            if 'id' in add.keys():
                if Address.objects.filter(id=add['id']).exists():
                    get_address = Address.objects.get(id=add['id'])
                    get_address.country = add.get('country', get_address.country)
                    get_address.province_city = add.get('province_city', get_address.province_city)
                    get_address.district = add.get('district', get_address.district)
                    get_address.ward = add.get('ward', get_address.ward)
                    get_address.name_street = add.get('name_street', get_address.name_street)
                    get_address.number = add.get('number', get_address.number)
                    get_address.save()
                else:
                    continue
            else:
                continue
        return instance


# ################################################### USER ############################################################

# ############################################## ADDRESS - APPENIX ####################################################

class GetCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id',
                  'name',
                  'code')


class GetProvinceCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProvinceCity
        fields = ('id',
                  'name',
                  'code')


class GetDistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ('id',
                  'name',
                  'code')


class GetWardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = ('id',
                  'name',
                  'code')

# ############################################## ADDRESS - APPENIX ####################################################
