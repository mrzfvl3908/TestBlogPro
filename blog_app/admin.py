from django.contrib import admin
from blog_app.models import Post,Category


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_filter = ['status']
    list_display = ['title','author', 'created_date', 'status']
    search_fields = ['title', 'short_description']
    empty_value_display = '-empty-'

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
