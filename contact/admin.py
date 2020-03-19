from django.contrib import admin
from .models import contactAdmin


class ContactAdminShow(admin.ModelAdmin):
    list_display = ('title_page', 'title_message','click')
    list_display_links = ( 'title_message', 'title_page' )
    list_filter = ('title_page',)
    search_fields = ('title_page','title_message')


admin.site.register(contactAdmin, ContactAdminShow)
