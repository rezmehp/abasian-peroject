from django.contrib import admin
from .models import classlinksAdmin,allclassLinks3


class classlinksAdminshow(admin.ModelAdmin):
    list_display = ('title_page', )
    
admin.site.register(classlinksAdmin, classlinksAdminshow)

class allclassLinks3show(admin.ModelAdmin):
    list_display = ('link_title',)
   
admin.site.register(allclassLinks3, allclassLinks3show)