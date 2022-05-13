from django.urls import path, include
from rest_framework.routers import SimpleRouter

from system.views import CountryManagementViewSet, ProvinceCityManagementViewSet, DistrictManagementViewSet, \
    WardManagementViewSet

router = SimpleRouter()
router.register('country-management-viewset', CountryManagementViewSet, basename="country-management-viewset")
router.register('province-city-management-viewset', ProvinceCityManagementViewSet, basename="province-city-management-viewset")
router.register('district-management-viewset', DistrictManagementViewSet, basename="district-management-viewset")
router.register('ward-management-viewset', WardManagementViewSet, basename="ward-management-viewset")


urlpatterns = [
    path("", include(router.urls)),
]
