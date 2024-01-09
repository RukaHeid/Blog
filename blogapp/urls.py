from django.urls import path
from . import views

app_name = "blogapp"

urlpatterns =[
    path("", views.IndexView.as_view(), name="index"),
    path("post/<int:pk>", views.PostDetailView.as_view(), name="post_detail"),
]