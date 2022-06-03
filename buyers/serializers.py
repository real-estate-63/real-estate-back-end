from rest_framework import serializers

from users.models import Address, RealEstate


class BuyerDetailAddressRealEstateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('country',
                  'province_city',
                  'district',
                  'ward',
                  'name_street',
                  'number')
        read_only_fields = ('country',
                            'province_city',
                            'district',
                            'ward',
                            'name_street',
                            'number')


class BuyerDetailRealEstateSerializer(serializers.ModelSerializer):
    address_real_estate = BuyerDetailAddressRealEstateSerializer()

    class Meta:
        model = RealEstate
        fields = ('name',
                  'type',
                  'type_sell',
                  'type_lease',
                  'price',
                  'area',
                  'description',
                  'image',
                  'status',
                  'address_real_estate',
                  )
        read_only_fields = ('name',
                            'type',
                            'type_sell',
                            'type_lease',
                            'price',
                            'area',
                            'description',
                            'image',
                            'status',
                            'address_real_estate',)


class BuyerListRealEstateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealEstate
        fields = ('id',
                  'name',
                  'type',
                  'description',
                  'image',
                  'status',
                  )
        read_only_fields = ('id',
                            'name',
                            'type',
                            'description',
                            'image',
                            'status',
                            'address_real_estate',)
