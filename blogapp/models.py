from django.db import models
from django.utils import timezone
from django.urls import reverse_lazy

# Create your models here.

class Blog(models.Model):
    blog_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.blog_name

        
    
class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    update_date = models.DateField("Last update", default=timezone.now)
    tags = models.ManyToManyField("Tag", blank=True, related_name="tags_on_post")
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title  
    
    def get_absolute_url(self):
        return reverse_lazy("blogapp:post_detail", args=[self.id])



class Tag(models.Model):
     tag_name = models.CharField(max_length=100)
     posts = models.ManyToManyField(Post, blank=True, related_name="posts_under_tag")
     
     def __str__(self):
        return self.tag_name
    

         
    
class Comment(models.Model):
    post = models.ForeignKey(Post,  on_delete=models.CASCADE)
    comments = models.TextField()
    comment_PostedDate = models.DateTimeField("Date of comments", default=timezone.now)
    name = models.CharField(max_length=100)
    
    def __str__(self):
         return f"{self.name}: {self.comments}"
    
    def get_absolute_url(self):
        return reverse_lazy("blogapp:comment", args=[self.id])
