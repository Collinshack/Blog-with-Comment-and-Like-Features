from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'Blog_Post/index.html', {'posts':posts})

def post_detail(request, slug):
    notify=False
    try:
        post = Post.objects.get(slug= slug)
    except Post.DoesNotExist:
        post = None
    
    if request.method == 'POST':
        
        if request.user.is_authenticated:
            user = request.user
            
            if post.post_likes.filter(id= user.id).exists():
                post.post_likes.remove(user)
                notify = False
                
            else:
                post.post_likes.add(user)
                notfiy = True     
    return render(request, 'Blog_Post/post_detail.html', { 'notify': notify, 'post':post})

def about(request):  
    return render(request, 'Blog_Post/about.html')

def contact(request):
    return render(request, 'Blog_Post/contact.html')