from django.shortcuts import render, get_object_or_404
from blog_app.models import Post, Category


def blog(request, author_username=None):
    posts = Post.objects.all()
    if author_username:
        posts = posts.filter(author__username=author_username)
    return render(request, 'blog_app/blog.html', {'posts': posts})


def single_blog(request,pid):
    post = get_object_or_404(Post, pk=pid)
    return render(request, 'blog_app/single_blog.html', {'post': post})


def blog_category(request,cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    return render(request, 'blog_app/blog.html', {'posts': posts})


def blog_search(request):
    posts = Post.objects.filter(status=1)
    if s := request.GET.get('s'):
        posts =posts.filter(description__contains=s)
    return render(request, 'blog_app/blog.html', {'posts': posts})