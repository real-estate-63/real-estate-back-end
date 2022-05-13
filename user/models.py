from django.contrib.auth.models import AbstractUser


from django.db import models


# Create your models here.
from system.models import District, Ward, Country, ProvinceCity


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    comparative_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        self.comparative_name = self.username
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'


class Address(models.Model):
    country_id = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    province_city_id = models.ForeignKey(ProvinceCity, on_delete=models.SET_NULL, null=True)
    district_id = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    ward_id = models.ForeignKey(Ward, on_delete=models.SET_NULL, null=True)
    name_street = models.CharField(max_length=64)
    number = models.CharField(max_length=5)
    full_address = models.CharField(max_length=256)

    def save(self, *args, **kwargs):
        self.full_address = self.number + ' ' + self.name_street + ',' + self.ward_id.name + ',' + self.district_id.name
        super(Address, self).save(*args, **kwargs)

    def __str__(self):
        return self.full_address

    class Meta:
        db_table = 'address'


class UserProfile(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    number_phone = models.CharField(max_length=14)
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'user_profile'


class RealEstateInfor(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    type = models.CharField(max_length=64)
    address_id = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images', blank=True)
    status = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'real_estate_infor'
