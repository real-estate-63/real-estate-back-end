from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

from django.db import models

# Create your models here.
from systems.models import District, Ward, Country, ProvinceCity, TypeSell, TypeLease


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


class RealEstate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    REALESTATE_TYPE_CHOICES = ((1, 'Sell'), (2, 'Lease'))
    type = models.IntegerField(choices=REALESTATE_TYPE_CHOICES, default=1)
    type_sell = models.ForeignKey(TypeSell, on_delete=models.SET_NULL, null=True)
    type_lease = models.ForeignKey(TypeLease, on_delete=models.SET_NULL, null=True)
    price = models.FloatField()
    area = models.FloatField()
    description = models.TextField()
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images', blank=True)
    REALESTATE_STATUS_CHOICES = ((1, 'New'), (2, 'Sold'))
    status = models.IntegerField(choices=REALESTATE_STATUS_CHOICES, default=1)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'real_estate'


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='address_profile')
    real_estate = models.OneToOneField(RealEstate, on_delete=models.CASCADE, null=True, blank=True, related_name='address_real_estate')
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
