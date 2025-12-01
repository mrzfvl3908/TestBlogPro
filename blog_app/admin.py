from django.contrib import admin
from blog_app.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title','status','created_date']
    date_hierarchy = 'created_date'
    search_fields = ['title', 'short_description']
    list_filter = ['status']
    empty_value_display = '-empty-'

admin.site.register(Post, PostAdmin)
