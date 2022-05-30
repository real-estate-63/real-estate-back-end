from rest_framework import status, viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from systems.models import Country, ProvinceCity, District, Ward
from systems.serializers import CountrySerializer, ProvinceSerializer, DistrictSerializer, WardSerializer


class CountryManagement(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    permission_classes = (IsAdminUser,)
    queryset = Country.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)  # ,many=True
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Register successful!'
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'error_message': serializer.errors,
                'errors_code': 400,
            }, status=status.HTTP_400_BAD_REQUEST)


class ProvinceCityManagement(viewsets.ModelViewSet):
    serializer_class = ProvinceSerializer
    permission_classes = (IsAdminUser,)
    queryset = ProvinceCity.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Register successful!'
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'error_message': serializer.errors,
                'errors_code': 400,
            }, status=status.HTTP_400_BAD_REQUEST)


class DistrictManagement(viewsets.ModelViewSet):
    serializer_class = DistrictSerializer
    permission_classes = (IsAdminUser,)
    queryset = District.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Register successful!'
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'error_message': serializer.errors,
                'errors_code': 400,
            }, status=status.HTTP_400_BAD_REQUEST)


class WardManagement(viewsets.ModelViewSet):
    serializer_class = WardSerializer
    permission_classes = (IsAdminUser,)
    queryset = Ward.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Register successful!'
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'error_message': serializer.errors,
                'errors_code': 400,
            }, status=status.HTTP_400_BAD_REQUEST)
