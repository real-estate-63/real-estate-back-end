from django.urls import path, include
from rest_framework.routers import SimpleRouter

from system.views import CountryManagement, ProvinceCityManagement, DistrictManagement, \
    WardManagement

router = SimpleRouter()
router.register('country-management', CountryManagement, basename="country-management")
router.register('province-city-management', ProvinceCityManagement, basename="province-city-management")
router.register('district-management', DistrictManagement, basename="district-management")
router.register('ward-management', WardManagement, basename="ward-management")


urlpatterns = [
    path("", include(router.urls)),
]
