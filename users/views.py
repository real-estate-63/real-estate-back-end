from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password

from rest_auth.registration.views import RegisterView
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from systems.models import Country, District, ProvinceCity, Ward
from users.serializers import UserSignUpSerializer, UserSignInSerializer, GetCountrySerializer, \
    GetProvinceCitySerializer, GetDistrictSerializer, GetWardSerializer, RegisterSerializer
from realEstateBackEnd import settings


# User register
class UserSignUpView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            serializer.save()

            return Response({
                'message': 'Register successful!'
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'error_message': serializer.errors,
                'errors_code': 400,
            }, status=status.HTTP_400_BAD_REQUEST)


# User login
class UserSignInView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserSignInSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                request,
                username=serializer.validated_data['comparative_name'],
                password=serializer.validated_data['password']
            )
            if user:
                refresh = TokenObtainPairSerializer.get_token(user)
                data = {
                    'refresh_token': str(refresh),
                    'access_token': str(refresh.access_token),
                    'access_expires': int(settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'].total_seconds()),
                    'refresh_expires': int(settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'].total_seconds())
                }
                login(request, user)
                return Response(data, status=status.HTTP_200_OK)

            return Response({
                'error_message': 'Username or password is incorrect!',
                'error_code': 400
            }, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            'error_messages': serializer.errors,
            'error_code': 400
        }, status=status.HTTP_400_BAD_REQUEST)


class UserRegisterView(RegisterView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


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
