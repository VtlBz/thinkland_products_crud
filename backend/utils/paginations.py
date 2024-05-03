from django.conf import settings
from rest_framework.pagination import PageNumberPagination


class ProductsPagination(PageNumberPagination):
    page_size = settings.DEFAULT_PAGE_SIZE
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = settings.DEFAULT_PAGE_SIZE
