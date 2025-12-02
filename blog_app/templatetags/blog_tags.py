from django import template
from django.db.models import Count, Q

from blog_app.models import Post, Category

register = template.Library()

@register.inclusion_tag('blog_app/includes/recent_posts.html')
def recent_posts():
    rec_posts = Post.objects.order_by('-created_date')[:3]
    return {'rec_posts': rec_posts}


@register.inclusion_tag('blog_app/includes/category_posts.html')
def category_posts():
    categories = Category.objects.annotate(
        post_count=Count('post', filter=Q(post__status=1))
    )
    return {'categories': categories}