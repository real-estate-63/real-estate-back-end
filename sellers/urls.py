from django.urls import path, include
from rest_framework.routers import SimpleRouter

from sellers.views import SellerManagementRealEstateViewSet

router = SimpleRouter()
router.register(r'seller_management_real_estate', SellerManagementRealEstateViewSet, basename="country_management")

urlpatterns = [
    path("", include(router.urls)),
]
