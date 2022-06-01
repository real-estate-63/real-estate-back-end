# ################################################# REAL ESTATE #######################################################
from rest_framework import viewsets, status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated

from sellers.permissions import IsSeller
from sellers.serializers import SellerManagementRealEstateSerializer
from rest_framework.response import Response

from users.models import RealEstate, UserProfile


class SellerManagementRealEstateViewSet(viewsets.ModelViewSet):
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = SellerManagementRealEstateSerializer
    permission_classes = (IsAuthenticated, IsSeller)
    queryset = RealEstate.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = self.request.user
            profile = UserProfile.objects.get(user=user)
            serializer.save(user=user, profile=profile)
            return Response({
                'message': 'Register successful!'
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'error_message': serializer.errors,
                'errors_code': 400,
            }, status=status.HTTP_400_BAD_REQUEST)
# ################################################# REAL ESTATE #######################################################
