from rest_framework.pagination import PageNumberPagination


class ApiPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "per_page"
