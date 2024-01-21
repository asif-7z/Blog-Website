from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination

class BlogPostOffLimitPagination(LimitOffsetPagination):
    default_limit = 4
    max_limit = 10

class BlogPostPageNumberPagiantion(PageNumberPagination):
    page_size = 4
    