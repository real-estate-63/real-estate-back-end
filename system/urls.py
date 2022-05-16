from django.urls import path, include
from rest_framework.routers import SimpleRouter

from system.views import CountryManagement, ProvinceCityManagement, DistrictManagement, \
    WardManagement

router = SimpleRouter()
router.register(r'^country_management/', CountryManagement, basename="country_management")
router.register(r'^province_city_management/', ProvinceCityManagement, basename="province_city_management")
router.register(r'^district_management/', DistrictManagement, basename="district_management")
router.register(r'^ward_management/', WardManagement, basename="ward_management")


urlpatterns = [
    path("", include(router.urls)),
]
