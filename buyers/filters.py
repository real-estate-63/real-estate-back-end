import django_filters

from users.models import RealEstate


class RealEstateFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='iexact')
    type = django_filters.CharFilter(field_name='type', lookup_expr='iexact')
    country = django_filters.NumberFilter(field_name='address_real_estate__country', lookup_expr='exact')
    province_city = django_filters.NumberFilter(field_name='address_real_estate__province_city', lookup_expr='exact')
    district = django_filters.NumberFilter(field_name='address_real_estate__district', lookup_expr='exact')
    ward = django_filters.NumberFilter(field_name='address_real_estate__ward', lookup_expr='exact')
