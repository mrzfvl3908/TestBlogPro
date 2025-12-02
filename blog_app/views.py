from django.shortcuts import render, get_object_or_404
from blog_app.models import Post, Category


def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog_app/blog.html', {'posts': posts})


def single_blog(request,pid):
    post = get_object_or_404(Post, pk=pid)
    return render(request, 'blog_app/single_blog.html', {'post': post})


def blog_category(request,cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    return render(request, 'blog_app/blog.html', {'posts': posts})