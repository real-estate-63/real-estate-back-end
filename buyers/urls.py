from django.conf.urls import url
from django.urls import path

from buyers.views import BuyerSearchRealEstateView, BuyerDetailRealEstateView

urlpatterns = [
    path('buyer_search_real_estate/', BuyerSearchRealEstateView.as_view(), name='buyer_search_real_estate'),
    url(r'^buyer_detail_real_estate/(?P<id>\d+)/$', BuyerDetailRealEstateView.as_view(), name='buyer_detail_real_estate')
]