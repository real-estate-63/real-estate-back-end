from rest_framework import serializers

from users.models import RealEstate, Address


class SellerManagementAddressRealEstateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Address
        fields = ('id',
                  'country',
                  'province_city',
                  'district',
                  'ward',
                  'name_street',
                  'number')
        read_only_fields = ('id',)


class SellerManagementRealEstateSerializer(serializers.ModelSerializer):

    class Meta:
        model = RealEstate
        fields = ('id',
                  'name',
                  'name',
                  'address',
                  'description',
                  'image',
                  'status')
