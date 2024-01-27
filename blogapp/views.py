from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
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
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = Comment.objects.filter(post=post)
        context["comment_list"] = comments
        return context
    

class CreatePostView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = "blogapp/create_post.html"



class CommentForm(CreateView):
    model = Comment
    fields = ["comments", "name"]
    context_object_name = "comment_list"
    
    def form_valid(self, form):
        post_id = self.kwargs['pk'] 
        post = get_object_or_404(Post, id=post_id)
        form.instance.post = post
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('blogapp:post_detail', args=[self.kwargs['pk']])
    
    
    
class UpdatePost(UpdateView):
    model = Post
    fields = ["title", "body", "author", "tags"]
    template_name = "blogapp/create_post.html"
    
    
class DeletePost(DeleteView):
    model = Post
    success_url = reverse_lazy("blogapp:index")