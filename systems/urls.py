from django.urls import path, include
from rest_framework.routers import SimpleRouter

from systems.views import CountryManagementViewSet, ProvinceCityManagementViewSet, DistrictManagementViewSet, \
    WardManagementViewSet

router = SimpleRouter()
router.register(r'country_management', CountryManagementViewSet, basename="country_management")
router.register(r'province_city_management', ProvinceCityManagementViewSet, basename="province_city_management")
router.register(r'district_management', DistrictManagementViewSet, basename="district_management")
router.register(r'ward_management', WardManagementViewSet, basename="ward_management")


urlpatterns = [
    path("", include(router.urls)),
]
