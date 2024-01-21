from django.urls import path

from .views import (BlogPost2ListApiView,
                    BlogPost2DetailView,
                    BlogPost2UpdateView,
                    BlogPost2DeleteView,
                    BlogPost2CreateView,)
app_name = "blogs-api"

urlpatterns = [
    path('create/',BlogPost2CreateView.as_view(),name="create"),
    path('',BlogPost2ListApiView.as_view(),name="posts"),
    path('<slug>/',BlogPost2DetailView.as_view(),name="detail"),
    path('<slug>/edit/',BlogPost2UpdateView.as_view(),name="edit"),
    path('<slug>/delete/',BlogPost2DeleteView.as_view(),name="delete"),


]


