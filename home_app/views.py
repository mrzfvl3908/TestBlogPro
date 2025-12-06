from django.shortcuts import render

from blog_app.models import Post


def index(request):
    posts = Post.objects.filter(status=1)
    if s := request.GET.get('s'):
        posts = posts.filter(description__contains=s)

    return render(request, 'home_app/index.html', {'posts': posts})
