from allauth.account.views import EmailView
from django.conf.urls import url
from django.urls import path, re_path
from rest_auth.registration.views import VerifyEmailView
from rest_auth.views import LogoutView

from users.views import UserLoginView, UserRegisterView, GetCountryView, GetProvinceCityView, \
    GetDistrictView, GetWardView, UserManagementProfile, ResendAuthEmailView

urlpatterns = [
    # ACCOUNT
    path('user_register/', UserRegisterView.as_view(), name='account_signup'),
    path(r'login/', UserLoginView.as_view(), name='account_login'),
    re_path(r'^logout/', LogoutView.as_view(), name="account_logout"),
    re_path(r'^email/', EmailView.as_view(), name="account_email"),
    re_path(r'^verify_email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(),
            name='account_confirm_email'),
    url(r'^resend_auth_email/', ResendAuthEmailView.as_view(), name="resend_auth_email"),

    # USER PROFILE
    path('user_management_profile/', UserManagementProfile.as_view(), name='UserManagementProfile'),

    # ADDRESS
    path('get_country/', GetCountryView.as_view(), name='get_country'),
    path('get_province_city/', GetProvinceCityView.as_view(), name='get_province_city_view'),
    path('get_district/<str:parent_code>/', GetDistrictView.as_view(), name='get_district_view'),
    path('get_ward/<str:parent_code>/', GetWardView.as_view(), name='get_ward'),

    # REAL ESTATE

]
