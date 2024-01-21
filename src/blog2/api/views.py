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
from blog2.models import BlogPost2
from .permissions import IsOwnerOrReady
from .serializers import BlogPost2Serializer,BlogPost2CreateUpdateSerializer,BlogPost2DetailSerializer
from django.db.models import Q
from rest_framework.filters import SearchFilter,OrderingFilter
from .pagination import BlogPostOffLimitPagination,BlogPostPageNumberPagiantion

class BlogPost2CreateView(CreateAPIView):
    queryset = BlogPost2.objects.all()
    serializer_class = BlogPost2CreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BlogPost2ListApiView(ListAPIView):
    serializer_class = BlogPost2Serializer
    queryset = BlogPost2.objects.all()
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['title2','slug']
    pagination_class = BlogPostPageNumberPagiantion


    def get_queryset(self,*args,**kwargs):
        query_list = BlogPost2.objects.all()
        query = self.request.GET.get("q")
        if query:
            query_list = query_list.filter(Q(title2__icontains =query)|Q(content2__icontains=query))
        return query_list



class BlogPost2DetailView(RetrieveAPIView):
    queryset = BlogPost2.objects.all()
    serializer_class = BlogPost2DetailSerializer
    lookup_field = 'slug'

class BlogPost2UpdateView(RetrieveUpdateAPIView):
    queryset = BlogPost2.objects.all()
    serializer_class = BlogPost2Serializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReady]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BlogPost2DeleteView(DestroyAPIView):
    queryset = BlogPost2.objects.all()
    serializer_class = BlogPost2Serializer
    lookup_field = 'slug'
