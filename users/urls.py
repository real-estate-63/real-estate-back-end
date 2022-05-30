from allauth.account.views import LoginView, LogoutView, EmailView
from allauth.socialaccount.views import SignupView
from django.urls import path, re_path
from rest_auth.registration.views import VerifyEmailView

from users.views import UserSignUpView, UserSignInView, UserRegisterView, GetCountryView, GetProvinceCityView, \
    GetDistrictView, GetWardView

urlpatterns = [
    # User Sign Up
    path(r'sign_up/', UserSignUpView.as_view(), name='sign_up'),
    # User Sign In
    path(r'sign_in/', UserSignInView.as_view(), name='sign_in'),

    path('user_register/', UserRegisterView.as_view(), name='user_register'),

    path(r'^login/', LoginView.as_view(), name="account_login"),
    path(r'^signup/', SignupView.as_view(), name="account_signup"),
    path(r'^logout/', LogoutView.as_view(), name="account_logout"),
    path(r'^logout/', EmailView.as_view(), name="account_email"),


    re_path(r'^verify_email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(),
            name='account_confirm_email'),

    path('get_country/', GetCountryView.as_view(), name='get_country'),

    path('get_province_city/', GetProvinceCityView.as_view(), name='get_province_city_view'),

    path('get_district/<str:parent_code>/', GetDistrictView.as_view(), name='get_district_view'),

    path('get_ward/<str:parent_code>/', GetWardView.as_view(), name='get_ward'),

]
