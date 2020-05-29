from django.contrib import admin
from .models import linksAdmin,allLinks


class linksAdminshow(admin.ModelAdmin):
    list_display = ('title_page', )
    
admin.site.register(linksAdmin, linksAdminshow)

class allLinksshow(admin.ModelAdmin):
    list_display = ('link_title',)
   
admin.site.register(allLinks, allLinksshow)