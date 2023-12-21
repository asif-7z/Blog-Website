from django.shortcuts import render
from .models import SearchQuery
from blog2.models import BlogPost2



# Create your views here.

def search_view(request):
    template_name = "search/view.html"
    query = request.GET.get('q')
    user = None
    if request.user.is_authenticated:
        user=request.user
        if query is not None:
            SearchQuery.objects.create(user=user,queryset=query)
            blog_list = BlogPost2.objects.search(query=query)
    context = {"query": query,"blog_list":blog_list}
    return render(request,template_name,context)        