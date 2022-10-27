from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255, default='coding')
    snippet = models.CharField(max_length=255)
    body = RichTextField(blank=True, null=True)
    # body = models.TextField()
    date_post = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return str(self.author.first_name ) +' '+ str(self.author.last_name) + ' | ' + self.title
    
    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})