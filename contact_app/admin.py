from django.contrib import admin
from contact_app.models import Contact


class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ['name', 'email']
    list_filter = ['name', 'email', 'subject']
    search_fields = ['name', 'email']

admin.site.register(Contact, ContactAdmin)