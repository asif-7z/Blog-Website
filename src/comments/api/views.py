from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.permissions import (IsAdminUser,
                                        IsAuthenticated,
                                        IsAuthenticatedOrReadOnly,
                                        AllowAny
                                        )
from comments.models import CommentSection
from blog2.api.permissions import IsOwnerOrReady
from .serializers import CommentSerializer,CommentsDetailSerializer
from django.db.models import Q
from rest_framework.filters import SearchFilter,OrderingFilter
from blog2.api.pagination import BlogPostOffLimitPagination,BlogPostPageNumberPagiantion

class CommentListView(ListAPIView):
    queryset = CommentSection.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['title','slug']
    pagination_class = BlogPostPageNumberPagiantion

    def get_queryset(self):
        # return super().get_queryset()
        query_list = CommentSection.objects.all()
        queryset = self.request.GET.get('q')
        if queryset:
            query_list = query_list.filter(Q(title__slug__icontains=queryset)|Q(text__icontains=queryset))
        return query_list


class CommentsDetailView(RetrieveAPIView):
    queryset = CommentSection.objects.all()
    serializer_class = CommentsDetailSerializer
    lookup_field = 'id'


    