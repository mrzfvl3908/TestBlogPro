from blog_app.models import Category

def sidebar_data(request):
    categories = Category.objects.all()
    return {
        'sidebar_categories': categories
    }