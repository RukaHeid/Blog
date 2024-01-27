from django.urls import path
from . import views

app_name = "blogapp"

urlpatterns =[
    path("", views.IndexView.as_view(), name="index"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("newpost/", views.CreatePostView.as_view(), name="create_post"),
    path("update/<int:pk>", views.UpdatePost.as_view(), name="update"),
    path("delete/<int:pk>", views.DeletePost.as_view(), name="delete"),
    path("comment/<int:pk>", views.CommentForm.as_view(), name="comment")

]