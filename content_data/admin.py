from django.contrib import admin
from .models import home, about, contact, work, footer
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'is_read']
    list_filter = ['is_read']
    list_editable = ['is_read']
    search_fields = ['text']

admin.site.register(home)
admin.site.register(about)
admin.site.register(contact, ContactAdmin)
admin.site.register(work)
admin.site.register(footer)