from django.shortcuts import render
from .models import CommentSection
from .form import CommentModel
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from blog2.models import BlogPost2
# Create your views here.

@login_required
@staff_member_required
def comments(request,slug):
    print("hello")
    template_name = "comment/comments.html"
    obj = BlogPost2.objects.get(slug=slug)
    print(obj)
    form = CommentModel(request.POST or None)
    if form.is_valid():
        if request.user.is_authenticated:
            form.save()
            form = CommentModel()
        else:
            print("not found")
    context = {"comment": form}
    return render(request,template_name,context)


def showcomments(request):
    temp = "comment/showcomments.html"
    obj = CommentSection.objects.all()
    context = {"object":obj}
    return render(request,temp,context)
