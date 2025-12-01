from django.contrib import admin
from contact_app.models import Contact


class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ['name', 'email', 'subject']
    list_filter = ['name', 'email', 'subject']
    search_fields = ['name', 'email','subject']

admin.site.register(Contact, ContactAdmin)