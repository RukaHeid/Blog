from django import forms
from .models import Post, Tag, Comment

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ["title", "author", "body", "tags", ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["tags"].widget = forms.SelectMultiple(attrs={"list":"tag_list"})
        self.fields["tags"].queryset = Tag.objects.all()
        