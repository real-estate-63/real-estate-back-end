from allauth.account import app_settings as allauth_settings
from allauth.account.utils import complete_signup
from django.http import Http404
from rest_auth.models import TokenModel

from rest_auth.registration.views import RegisterView
from rest_auth.views import LoginView
from rest_framework import status, viewsets
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from systems.models import Country, District, ProvinceCity, Ward
from users.models import UserProfile
from users.serializers import GetCountrySerializer, \
    GetProvinceCitySerializer, GetDistrictSerializer, GetWardSerializer, RegisterSerializer, \
    UserManagementProfileSerializer, UserLoginSerializer, ResendAuthEmailSerializer


# ################################################## ACCOUNT ##########################################################
class UserRegisterView(RegisterView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class UserLoginView(LoginView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer
    token_model = TokenModel


class ResendAuthEmailView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ResendAuthEmailSerializer

    def post(self, request, *args, **kwargs):
        complete_signup(self.request._request, self.request.user,
                        allauth_settings.EMAIL_VERIFICATION, None)
        return Response({"detail": "Successful"}, status=status.HTTP_200_OK)


# ################################################## ACCOUNT ##########################################################

# #################################################### USER ###########################################################
class UserManagementProfile(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserManagementProfileSerializer

    def get_object(self, request):
        user = request.user
        if UserProfile.objects.filter(user=user).exists():
            return UserProfile.objects.get(user=user)
        else:
            raise Http404()

    def get(self, request):
        userprofile = self.get_object(request)
        serializer = self.serializer_class(userprofile).data
        return Response(serializer)

    def put(self, request):
        userprofile = self.get_object(request)
        serializer = self.serializer_class(userprofile, data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Register successful!'
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# #################################################### USER ###########################################################


# ############################################## ADDRESS - APPENIX ####################################################
class GetCountryView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Country.objects.filter(code=84)
    serializer_class = GetCountrySerializer


class GetProvinceCityView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = ProvinceCity.objects.all()
    serializer_class = GetProvinceCitySerializer


class GetDistrictView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = GetDistrictSerializer
    lookup_url_kwarg = "parent_code"

    def get_queryset(self):
        parent_code = self.kwargs.get(self.lookup_url_kwarg)
        query = District.objects.filter(parent_code=parent_code)
        return query


class GetWardView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = GetWardSerializer
    lookup_url_kwarg = "parent_code"

    def get_queryset(self):
        parent_code = self.kwargs.get(self.lookup_url_kwarg)
        query = Ward.objects.filter(parent_code=parent_code)
        return query
# ############################################## ADDRESS - APPENIX ####################################################



