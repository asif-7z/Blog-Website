from django.urls import path
from .views import(CommentListView,
                   CommentsDetailView,
                   CreateCommentView,
)
app_name = "comment-apis"
urlpatterns = [
    path('',CommentListView.as_view(),name="list"),
    path('<int:id>/',CommentsDetailView.as_view(),name="detail"),
    path('create/',CreateCommentView.as_view(),name='create'),
]