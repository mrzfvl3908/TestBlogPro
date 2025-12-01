from django.urls import path
from . import views

app_name = 'blog_app'
urlpatterns = [
    path('', views.blog, name='blog'),
    path('single', views.single_blog, name='single_blog'),
]
