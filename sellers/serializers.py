from rest_framework import serializers

from users.models import RealEstate, Address


class SellerManagementAddressRealEstateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ('id',
                  'user',
                  'profile',
                  'country',
                  'province_city',
                  'district',
                  'ward',
                  'name_street',
                  'number')
        read_only_fields = ('id',
                            'user',
                            'profile',
                            )


class SellerManagementRealEstateSerializer(serializers.ModelSerializer):
    address_real_estate = SellerManagementAddressRealEstateSerializer()

    class Meta:
        model = RealEstate
        fields = ('id',
                  'name',
                  'type',
                  'description',
                  'image',
                  'status',
                  'address_real_estate',
                  )
        read_only_fields = ('id',)

    def create(self, validated_data):
        address_real_estate_data = validated_data.pop('address_real_estate')
        real_estate = RealEstate.objects.create(**validated_data)
        Address.objects.create(**address_real_estate_data,
                               user=real_estate.user,
                               profile=real_estate.profile,
                               real_estate=real_estate)
        return real_estate

    def update(self, instance, validated_data):
        # update real estate
        instance.name = validated_data.get('name', instance.name)
        instance.type = validated_data.get('type', instance.type)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        # update address
        address_real_estate_data = validated_data.pop('address_real_estate')
        instance.address_real_estate.country = address_real_estate_data.get('country')
        instance.address_real_estate.province_city = address_real_estate_data.get('province_city')
        instance.address_real_estate.district = address_real_estate_data.get('district')
        instance.address_real_estate.ward = address_real_estate_data.get('ward')
        instance.address_real_estate.name_street = address_real_estate_data.get('name_street')
        instance.address_real_estate.number = address_real_estate_data.get('number')
        instance.address_real_estate.save()
        return instance
