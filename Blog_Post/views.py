from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post
from .forms import CommentForm 
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'Blog_Post/index.html', {'posts':posts})

def post_detail(request, slug):
    post = Post.objects.get(slug= slug)
    comments = post.comments.all()   
    new_comment = None
    notify=False
    if request.user.is_authenticated:
        user = request.user
        if post.post_likes.filter(id=user.id).exists():
            notify = True

    if request.method == 'POST':
        comments = post.comments.all()
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return HttpResponseRedirect(reverse('post_detail', args=[str(post.slug)]))
        if request.user.is_authenticated:
            user = request.user
            
            if post.post_likes.filter(id= user.id).exists():
                notify = False                
                post.post_likes.remove(user)
                
                
            else:
                notfiy = True 
                post.post_likes.add(user)
                
    else:
        form = CommentForm()
    return render(request, 'Blog_Post/post_detail.html', { 'notify': notify, 'post':post, 'comments': comments, 'form':form})


def about(request):  
    return render(request, 'Blog_Post/about.html')

def contact(request):
    return render(request, 'Blog_Post/contact.html')

