from django.urls import path

from user.views import UserSignUpView, UserSignInView

urlpatterns = [
    # User Sign Up
    path('sign_up/', UserSignUpView.as_view(), name='sign_up'),
    # User Sign In
    path('sign_in/', UserSignInView.as_view(), name='sign_in'),
]