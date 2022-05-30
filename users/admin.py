from django.contrib import admin

# Register your models here.
from users.models import User, Address, UserProfile, RealEstateInfor

admin.site.register(User)
admin.site.register(Address)
admin.site.register(UserProfile)
admin.site.register(RealEstateInfor)

