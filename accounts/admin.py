from django.contrib import admin
from .models import karbaruser1

class karbaruser1show(admin.ModelAdmin):
    list_display = ('username', 'email','tell','maghta','reshte','ostan','shahr',)
    list_filter = ('maghta','reshte','ostan','shahr',)
   
    

admin.site.register(karbaruser1, karbaruser1show)