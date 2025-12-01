from django.shortcuts import render

def blog(request):
    return render(request, 'blog_app/blog.html', {})


def single_blog(request):
    return render(request, 'blog_app/single_blog.html', {})
