from django.contrib import admin

# Register your models here.
from user.models import User, Location, UserProfile, RealEstateInfor

admin.site.register(User)
admin.site.register(Location)
admin.site.register(UserProfile)
admin.site.register(RealEstateInfor)

