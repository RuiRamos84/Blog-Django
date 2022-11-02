from django import forms

from .models import Category, Post, Comment

choices = Category.objects.all().values_list('name', 'name')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category',
                  'snippet', 'body', 'header_image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title Tag'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username', 'id': 'elder', 'type': 'hidden'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control', 'placeholder': 'Category'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Snippet'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comment'}),
        }

