from django.shortcuts import get_object_or_404, redirect, render
from .models import BlogPost2,LogIn
from django.http import Http404
from .forms import CreateForm,LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
def blog2_post_page(request,slug):
    try:
        obj = BlogPost2.objects.get(slug=slug) # for single object return
        #or 
        ##queryset = BlogPost2.objects.filter(slug=slug) ## for multiple object return
        ##obj = queryset.first()
    except BlogPost2.DoesNotExist:
        raise Http404
    except ValueError:
        raise Http404
    template_name = "blog2_post_page.html"
    context = {"object2": obj}
    return render(request,template_name,context)

def blog_post_list_view(request):
    template_name = "blog2/list.html"
    obj = BlogPost2.objects.all().published()
    if request.user.is_authenticated:
        my_qs = BlogPost2.objects.filter(user=request.user)
        obj = (obj | my_qs)
    context = {"objects":obj}
    return render(request,template_name,context)

@login_required(login_url='/login/')
@staff_member_required
def blog_post_create_view(request):
    form = CreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj= form.save(commit=False)
        obj.user = request.user
        obj.save()
       # obj = BlogPost2.objects.create(**form.cleaned_data)
        form = CreateForm()
     
    template_name = "form.html"
    context = {"form":form}
    return render(request,template_name,context)


def blog_post_detail_view(request,slug):
    template_name = "blog2/detail.html"
    obj = BlogPost2.objects.get(slug=slug)
    context = {"objects":obj}
    return render(request,template_name,context)


@staff_member_required
def blog_post_update_view(request,slug):
    obj = get_object_or_404(BlogPost2,slug=slug)
    form = CreateForm(request.POST or None,request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = "form.html"
    context = {"form":form,"title":obj.title2}
    return render(request,template_name,context)


@staff_member_required
def blog_post_delete_view(request,slug):
    template_name = "blog2/delete.html"
    obj = get_object_or_404(BlogPost2,slug=slug)
    if request.method == "POST":
        obj.delete()
        return  redirect("/blog2/")
    context = {"objects":obj}
    return render(request,template_name,context)



def login(request):
    temp_name = "form.html"
    form = LoginForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        #obj = LogIn.objects.create(**form.cleaned_data)
        form = LoginForm()
    context = {"login":form}
    return render(request,temp_name,context)


