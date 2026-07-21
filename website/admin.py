from django.contrib import admin
from website.models import Contact
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = 'empty'
    #fields = ('name', )
    #exclude = ('subject', )
    list_display = ('name', 'id', 'email', 'subject', 'created_date')
    list_filter = ('name', )
    ordering = ['name']
    search_fields = ['name', 'message']



admin.site.register(Contact, ContactAdmin)


