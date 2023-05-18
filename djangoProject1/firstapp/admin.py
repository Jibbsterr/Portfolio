from django.contrib import admin
from firstapp.models import Contact
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'concern')  # Add fields to display in "Database Contents" view

admin.site.register(Contact, ContactAdmin)