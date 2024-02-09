from django.urls import path,include
from .views import comment_thread,delete_comment
urlpatterns = [

path('<id>/comment_thread/',comment_thread,name="thread"),
path('<id>/delete/',delete_comment)

]