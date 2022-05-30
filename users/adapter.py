from allauth.account.adapter import DefaultAccountAdapter

from systems.models import Country, ProvinceCity, District, Ward
from users.models import UserProfile, Address


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        user = super(CustomAccountAdapter,
                     self).save_user(request, user, form, commit)
        data = form.cleaned_data
        country = Country.objects.get(code=data['country_id'])
        province_city_id = ProvinceCity.objects.get(code=data['province_city_id'])
        district_id = District.objects.get(code=data['district_id'])
        ward_id = Ward.objects.get(code=data['ward_id'])
        address = Address(user_id=user,
                          country_id=country,
                          province_city_id=province_city_id,
                          district_id=district_id,
                          ward_id=ward_id,
                          name_street=data['name_street'],
                          number=data['number']).save()
        UserProfile(user_id=user,
                    first_name=data['first_name'],
                    middle_name=data['middle_name'],
                    last_name=data['last_name'],
                    phone_number=data['phone_number'],
                    birth_date=data['birth_date'],
                    adress_id=address
                    ).save()
        return user
