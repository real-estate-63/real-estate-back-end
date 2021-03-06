from allauth.account.adapter import DefaultAccountAdapter

from systems.models import Country, ProvinceCity, District, Ward
from users.models import UserProfile, Address


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        from allauth.account.utils import user_email
        data = form.cleaned_data
        email = data.get('email')
        user_type = data.get('user_type')
        user_email(user, email)
        if user_type:
            user.user_type = data.get('user_type')
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            # Ability not to commit makes it easier to derive from
            # this adapter by adding
            user.save()
        # Address
        country = Country.objects.get(code=data['country'])
        province_city = ProvinceCity.objects.get(code=data['province_city'])
        district = District.objects.get(code=data['district'])
        ward = Ward.objects.get(code=data['ward'])
        # Profile
        profile = UserProfile(user=user,
                              first_name=data['first_name'],
                              middle_name=data['middle_name'],
                              last_name=data['last_name'],
                              phone_number=data['phone_number'],
                              birth_date=data['birth_date'])
        profile.save()
        Address(user=user,
                profile=profile,
                country=country,
                province_city=province_city,
                district=district,
                ward=ward,
                name_street=data['name_street'],
                number=data['number']).save()
        return user
