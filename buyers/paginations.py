from rest_framework.pagination import PageNumberPagination


class PaginationListRealEstate(PageNumberPagination):
    page_size_query_param = 'size'
