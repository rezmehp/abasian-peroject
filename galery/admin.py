from django.contrib import admin
from .models import galerys,galerysAdmin


class galerysAdminshow(admin.ModelAdmin):
    list_display = ('title_page', )
    
admin.site.register(galerysAdmin, galerysAdminshow)

class galerysshow(admin.ModelAdmin):
    list_display = ('title',)
   
admin.site.register(galerys, galerysshow)