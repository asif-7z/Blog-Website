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
from .serializers import CommentSerializer,CommentsDetailSerializer,create_comment_serializer,CommentListSerializer
from django.db.models import Q
from rest_framework.filters import SearchFilter,OrderingFilter
from blog2.api.pagination import BlogPostOffLimitPagination,BlogPostPageNumberPagiantion
from rest_framework.mixins import DestroyModelMixin,UpdateModelMixin


class CreateCommentView(CreateAPIView):
    queryset = CommentSection.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        model_type = self.request.GET.get('type')
        slug = self.request.GET.get('slug')
        parent_id = self.request.GET.get('parent_id',None)
        return create_comment_serializer(model_type=model_type,
                                         slug=slug,parent_id=parent_id,
                                         user=self.request.user)

class CommentListView(ListAPIView):
    queryset = CommentSection.objects.all()
    serializer_class = CommentListSerializer
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
    # def get_comments(self):
    #     query_list = CommentSection.objects.filter_blog_obj()




class CommentsDetailView(RetrieveAPIView,DestroyModelMixin,UpdateModelMixin):
    queryset = CommentSection.objects.filter(id__gte=0)
    serializer_class = CommentsDetailSerializer
    lookup_field = 'id'
    permission_classes = [IsOwnerOrReady]

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
                            