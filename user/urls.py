from django.urls import path

from user.views import UserSignUpView, UserSignInView

urlpatterns = [
    # User Sign Up
    path('sign-up', UserSignUpView.as_view(), name='sign-up'),
    # User Sign In
    path('sign-in', UserSignInView.as_view(), name='sign-in'),
]