from django.urls import path
from .views import CommentListView,CommentsDetailView

app_name = "comment-apis"
urlpatterns = [
    path('',CommentListView.as_view(),name="list"),
    path('<int:id>/details/',CommentsDetailView.as_view(),name="detail"),
]