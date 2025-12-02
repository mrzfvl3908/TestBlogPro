from django import template
from blog_app.models import Post

register = template.Library()

@register.inclusion_tag('blog_app/includes/recent_posts.html')
def recent_posts():
    rec_posts = Post.objects.order_by('-created_date')[:3]
    return {'rec_posts': rec_posts}