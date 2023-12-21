"""
URL configuration for Myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .view import home,page,about,home_page,contact
from blog.views import blog_post_page
from blog2.views import blog_post_create_view,login
from search.views import search_view
from django.conf import settings
from comments.views import comments,showcomments
urlpatterns = [
 #   path('blog/',blog_post_page),
    path('blog/<int:post_id>/',blog_post_page),
    path('blog2/login/',login),
    path('blog2/create/',blog_post_create_view),

    path('blog2/',include('blog2.urls')),
    path('',home_page),
    path('home/',home),
    path('page/',page),
    path('about/',about),
    path('contactus/',contact),
    path('search/',search_view),
    path('blog2/<str:slug>/',comments),
    path('show/',showcomments),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)