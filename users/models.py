from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

from django.db import models

from enum import Enum

# Create your models here.
from systems.models import District, Ward, Country, ProvinceCity


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("the given email must be set")
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    first_name = None
    last_name = None
    email = models.EmailField(unique=True)
    USER_TYPE_CHOICES = ((1, 'Sell'), (2, 'Buy'))
    user_type = models.IntegerField(choices=USER_TYPE_CHOICES, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'users'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    full_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=14)
    birth_date = models.DateField()

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'user_profile'

    def save(self, *args, **kwargs):
        self.full_name = '%s %s %s' % (self.first_name, self.middle_name, self.last_name)
        super(UserProfile, self).save(*args, **kwargs)


class SetTypeSell(Enum):
    PRIVATE_HOUSE = 1
    APARTMENT = 2
    VILLA_TOWNHOUSE = 3
    HOUSE_STREET = 4
    SHOPHOUSE_COMMERCIAL = 5
    PROJECT_LAND = 6
    SOIL = 7
    FARM_RESORT = 8
    WAREHOUSE_FACTORY = 9
    DIFFERENT = 10

    def __str__(self):
        if self is self.PRIVATE_HOUSE:
            return "Bán nhà riêng"
        elif self is self.APARTMENT:
            return "Bán căn hộ chung cư"
        elif self is self.VILLA_TOWNHOUSE:
            return "Bán biệt thự, nhà liền kề"
        elif self is self.HOUSE_STREET:
            return "Bán nhà mặt phố"
        elif self is self.SHOPHOUSE_COMMERCIAL:
            return "Bán shophouse, nhà phố thương mại"
        elif self is self.PROJECT_LAND:
            return "Bán đất nền dự án"
        elif self is self.SOIL:
            return "Bán đất"
        elif self is self.FARM_RESORT:
            return "Bán trang trại, khu nghỉ dưỡng"
        elif self is self.WAREHOUSE_FACTORY:
            return "Bán kho, nhà xưởng"
        elif self is self.DIFFERENT:
            return "Bán loại bất động sản khác"
        else:
            raise RuntimeError("unexpected value %d" % self.value)

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def choices():
        return [(s_type.value, str(s_type)) for s_type in SetTypeSell]


class SetTypeLease(Enum):
    PRIVATE_HOUSE = 1
    APARTMENT = 2
    VILLA_TOWNHOUSE = 3
    HOUSE_STREET = 4
    SHOPHOUSE_COMMERCIAL = 5
    INN_ROOM = 6
    OFFICE = 7
    SHOP_KIOSK = 8
    WAREHOUSE_FACTORY = 9
    SOIL = 10
    DIFFERENT = 11

    def __str__(self):
        if self is self.PRIVATE_HOUSE:
            return "Cho thuê nhà riêng"
        elif self is self.APARTMENT:
            return "Cho thuê căn hộ chung cư"
        elif self is self.VILLA_TOWNHOUSE:
            return "Cho thuê biệt thự, nhà liền kề"
        elif self is self.HOUSE_STREET:
            return "Cho thuê nhà mặt phố"
        elif self is self.SHOPHOUSE_COMMERCIAL:
            return "Cho thuê shophouse, nhà phố thương mại"
        elif self is self.INN_ROOM:
            return "Cho thuê nhà trọ, phòng trọ"
        elif self is self.OFFICE:
            return "Cho thuê văn phòng"
        elif self is self.SHOP_KIOSK:
            return "Cho thuê cửa hàng, ki ốt"
        elif self is self.WAREHOUSE_FACTORY:
            return "Cho thuê kho, nhà xưởng, đất"
        elif self is self.SOIL:
            return "Cho thuê đất"
        elif self is self.DIFFERENT:
            return "Cho thuê loại bất động sản khác"
        else:
            raise RuntimeError("unexpected value %d" % self.value)

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def choices():
        return [(s_type.value, str(s_type)) for s_type in SetTypeLease]


class RealEstate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    REALESTATE_TYPE_CHOICES = ((1, 'Sell'), (2, 'Lease'))
    type = models.IntegerField(choices=REALESTATE_TYPE_CHOICES, default=1)
    type_sell = models.IntegerField(choices=SetTypeSell.choices(), blank=True, null=True)
    type_lease = models.IntegerField(choices=SetTypeLease.choices(), blank=True, null=True)
    price = models.FloatField()
    area = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='images', blank=True)
    REALESTATE_STATUS_CHOICES = ((1, 'New'), (2, 'Sold'))
    status = models.IntegerField(choices=REALESTATE_STATUS_CHOICES, default=1)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'real_estate'


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='address_profile')
    real_estate = models.OneToOneField(RealEstate, on_delete=models.CASCADE, null=True, blank=True,
                                       related_name='address_real_estate')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    province_city = models.ForeignKey(ProvinceCity, on_delete=models.SET_NULL, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    ward = models.ForeignKey(Ward, on_delete=models.SET_NULL, null=True)
    name_street = models.CharField(max_length=64)
    number = models.CharField(max_length=5)
    full_address = models.CharField(max_length=256)

    def save(self, *args, **kwargs):
        self.full_address = '%s, %s, %s, %s' % (self.number, self.name_street, self.ward.name, self.district.name)
        super(Address, self).save(*args, **kwargs)

    def __str__(self):
        return self.full_address

    class Meta:
        db_table = 'address'
