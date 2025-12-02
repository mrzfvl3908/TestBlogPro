from django.urls import path
from . import views

app_name = 'blog_app'
urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:pid>', views.single_blog, name='single_blog'),
    path('category/<str:cat_name>', views.blog_category, name='category'),
]
