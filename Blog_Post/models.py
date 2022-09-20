import email
from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    featured_image = models.ImageField(upload_to='Post_Images', blank=True)
    title = models.CharField(max_length=50)
    body = models.TextField()
    slug = models.SlugField()
    date_published = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authors')
    post_likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    comment_body = models.TextField(blank=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    
    def __str__(self):
        return f'{self.name} commented on {self.post}'
    
    