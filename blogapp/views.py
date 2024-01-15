from django.shortcuts import render
from django.views import generic 
from blogapp.models import Blog, Post, Comment, Tag, Author

# Create your views here.

class IndexView(generic.ListView):
    template_name = "blogapp/index.html"
    context_object_name = "post_list"
    
    def get_queryset(self):
        return Post.objects.all().order_by("-update_date")

class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blogapp/detail.html"