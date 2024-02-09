from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from .forms import ContactForm
from blog2.models import BlogPost2

msg = "hello devil"
def home(request):
    return HttpResponse("<h1>hello</h1>")

def home_page(request):
    my_title = "Welcome to Devil's Blog"
    temp_name = "home.html"
    obj = BlogPost2.objects.all()[:2]
    context = {"title": my_title, "blog_post":obj}
    return render(request,temp_name,context)


def page(request):

    return render(request,'hello.html',{"title":msg,"list":[1,2,3,4,5]})

def about(request):
    return render(request,'about.html',{"title":"About Us"})

def contact(request):
    print(request.POST)
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {"title": "contact us","form":form}
    return render(request,'form.html',context)