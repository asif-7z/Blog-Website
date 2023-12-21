from django.shortcuts import render,get_list_or_404
from django.http import Http404

from .models import BlogPost
# Create your views here.

def blog_post_page(request,post_id):
    try:
        obj = BlogPost.objects.get(id=str(post_id))
    except BlogPost.DoesNotExist:
        raise Http404
    except ValueError:
        raise Http404
    template_name = "blog_post_page.html"
    context = {"object": obj}
    return render(request,template_name,context)


