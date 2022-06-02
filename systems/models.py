from django.db import models


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=128)
    slug = models.CharField(max_length=128)
    type = models.CharField(max_length=64)
    name_with_type = models.CharField(max_length=64)
    code = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'country'


class ProvinceCity(models.Model):
    name = models.CharField(max_length=128)
    slug = models.CharField(max_length=128)
    type = models.CharField(max_length=64)
    name_with_type = models.CharField(max_length=64)
    code = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'province_city'


class District(models.Model):
    name = models.CharField(max_length=128)
    slug = models.CharField(max_length=128)
    type = models.CharField(max_length=64)
    name_with_type = models.CharField(max_length=64)
    code = models.CharField(max_length=64)
    parent_code = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'district'


class Ward(models.Model):
    name = models.CharField(max_length=128)
    slug = models.CharField(max_length=128)
    type = models.CharField(max_length=64)
    name_with_type = models.CharField(max_length=64)
    code = models.CharField(max_length=64)
    parent_code = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ward'


class TypeSell(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'type_sell'


class TypeLease(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'type_lease'
