from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination


class BookPagination(PageNumberPagination):
    page_size=3
    page_size_query_param="page_size"
    max_page_size=10



class LimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 10