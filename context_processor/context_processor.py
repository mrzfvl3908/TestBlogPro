from django.db.models import Count, Q
from blog_app.models import Category

def category_posts(request):
    categories = Category.objects.annotate(
        post_count=Count('post', filter=Q(post__status=1))
    )
    return {'categories': categories}