from typing import Any
from django.shortcuts import render, redirect
from django.views import generic 
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from blogapp.models import Blog, Post, Comment, Tag, Author
from django.urls import reverse_lazy
from .forms import PostForm



# Create your views here.

class IndexView(generic.ListView):
    template_name = "blogapp/index.html"
    context_object_name = "post_list"
    
    def get_queryset(self):
        return Post.objects.all().order_by("-update_date")
    

class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blogapp/detail.html"


def CreatePost(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect("blogapp:post_detail", post.id)
    else:
        form = PostForm()
        context = {
            "form" : form,
            "tags" : Tag.objects.all(),
        }
    return render(request, "blogapp/create_post.html", context)


class CommentForm(CreateView):
    model = Comment
    fields = ["comments", "name"]
    context_object_name = "comment_list"
    
    
class UpdatePost(UpdateView):
    model = Post
    fields = ["title", "body", "author", "tags"]
    
    
class DeletePost(DeleteView):
    model = Post
    success_url = reverse_lazy("blogapp:index")