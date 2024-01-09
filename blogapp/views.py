from django.shortcuts import render
from django.views import generic 
from blogapp.models import Blog, Post, Comment, Tag, Author

# Create your views here.

class IndexView(generic.ListView):
    template_name = "blogapp/index.htlm"
    context_object_name = "latest_post_list"
    queryset = Post.objects.all()

class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blogapp/detail.html"