from django.shortcuts import render
from django.views import generic 
from django.views.generic.edit import CreateView, DeleteView, UpdateView
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


class NewPostForm(CreateView):
    model = Post
    fields = ["title", "body", "author", "tags"]


class CommentForm(CreateView):
    model = Comment
    fields = ["comments", "name"]
    context_object_name = "comment_list"
    
    
class UpdatePost(UpdateView):
    model = Post
    fields = ["title", "body", "author", "tags"]
    
    
class DeletePost(DeleteView):
    model = Post
    success_url = "blogapp:post_detail.html"