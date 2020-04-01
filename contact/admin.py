from django.contrib import admin
from .models import contactAdmin,contactuserpm


class ContactAdminShow(admin.ModelAdmin):
    list_display = ('title_page', 'title_message','click')
    list_display_links = ( 'title_message', 'title_page' )
    list_filter = ('title_page',)
    


admin.site.register(contactAdmin, ContactAdminShow)

class contactuserpmshow(admin.ModelAdmin):
    list_display = ('usernamefkey', 'javabadmin')
    list_display_links = ( 'usernamefkey', )
    list_filter = ('usernamefkey',)


admin.site.register(contactuserpm, contactuserpmshow)