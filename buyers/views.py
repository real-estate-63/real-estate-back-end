from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from buyers.filters import RealEstateFilter
from buyers.paginations import PaginationListRealEstate
from buyers.serializers import BuyerListRealEstateSerializer, BuyerDetailRealEstateSerializer
from users.models import RealEstate
from django_filters import rest_framework as filters


class BuyerSearchRealEstateView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = RealEstate.objects.all()
    serializer_class = BuyerListRealEstateSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = RealEstateFilter
    pagination_class = PaginationListRealEstate

    def list(self, request, *args, **kwargs):
        query = self.filter_queryset(self.queryset)
        page = self.paginate_queryset(query)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.serializer_class(query, many=True)
        return Response(serializer.data)


class BuyerDetailRealEstateView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    queryset = RealEstate.objects.all()
    serializer_class = BuyerDetailRealEstateSerializer
