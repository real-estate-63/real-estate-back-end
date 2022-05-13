from django.contrib import admin

# Register your models here.

from system.models import District, Ward, ProvinceCity, Country

admin.site.register(Country)
admin.site.register(ProvinceCity)
admin.site.register(District)
admin.site.register(Ward)
