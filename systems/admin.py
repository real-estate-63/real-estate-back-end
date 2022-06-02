from django.contrib import admin

# Register your models here.

from systems.models import District, Ward, ProvinceCity, Country, TypeSell, TypeLease

admin.site.register(Country)
admin.site.register(ProvinceCity)
admin.site.register(District)
admin.site.register(Ward)
admin.site.register(TypeSell)
admin.site.register(TypeLease)