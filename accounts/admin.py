from django.contrib import admin
from .models import karbaruser1

class karbaruser1show(admin.ModelAdmin):
    list_display = ('username', 'email','tell',)
    search_fields = ('username',)
   
    

admin.site.register(karbaruser1, karbaruser1show)