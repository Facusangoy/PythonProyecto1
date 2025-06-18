from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'AppBlog/index.html', {'posts': posts})

def detalle_post(request, id):
    post = Post.objects.get(pk=id)
    return render(request, 'AppBlog/detalle_post.html', {'post': post})