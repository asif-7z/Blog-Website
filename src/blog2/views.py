from django.shortcuts import get_object_or_404, redirect, render
from .models import BlogPost2,LogIn
from django.http import Http404
from .forms import CreateForm,LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from comments.form import CommentModel
from comments.models import CommentSection
from django.contrib.contenttypes.models import ContentType


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
      # Show 25 contacts per page.

    
    obj = BlogPost2.objects.all().published()
   
    if request.user.is_authenticated:
        my_qs = BlogPost2.objects.filter(user=request.user)
        objs = (obj | my_qs)
        paginator = Paginator(objs,3)
        page_number = request.GET.get("page")
        try:
            obj = paginator.get_page(page_number)  # returns the desired page object
        except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
            obj = paginator.page(1)
        except EmptyPage:
        # if page is empty then return last page
            obj = paginator.page(paginator.num_pages)
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
    intial_data = {"content_type":obj.get_content_type,
              "object_id":obj.id}
    form = CommentModel(request.POST or None,initial=intial_data)
    if form.is_valid():
        c_type = form.cleaned_data.get('content_type')
        content_type_model = ContentType.objects.get_for_model(obj.__class__)
        o_id = form.cleaned_data.get('object_id')
        text = form.cleaned_data.get('text')
        parent_id = request.POST.get('parent_id')
        parent_obj = None
        try:
            parent_id = int(request.POST.get('parent_id'))
        except:
            parent_id = None
        if parent_id:
            parent_qs= CommentSection.objects.filter(id =parent_id)
            if parent_qs:
                parent_obj = parent_qs.first()
        if request.user.is_authenticated:
            new_obj,obj1 = CommentSection.objects.get_or_create(user=request.user,
                                                                content_type=content_type_model,
                                                                object_id = o_id,
                                                                parent=parent_obj,
                                                                text= text)
            form = CommentModel()
            return redirect('.')
        else:
            print("not found")

    
    content_type = ContentType.objects.get_for_model(obj)

    obj_id = obj.id
    comment = obj.comments
    #delete Comment     
 
    # comment_obj = CommentSection.objects.filter(title__slug=slug)
    context = {"objects":obj,"comment":form,"c_obj":comment}
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


