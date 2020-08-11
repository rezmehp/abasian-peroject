from django.contrib import admin
from .models import news,newsAdmin


class newsAdminshow(admin.ModelAdmin):
    list_display = ('title_page', )
    
admin.site.register(newsAdmin, newsAdminshow)

class newsshow(admin.ModelAdmin):
    list_display = ('title',)
   
admin.site.register(news, newsshow)