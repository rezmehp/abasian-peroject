from django.contrib import admin
from .models import buys

class buysshow(admin.ModelAdmin):
    list_display = ('userid','username','address','email','mobile','coursetype','courseid','coursename','description','amount',)
    list_filter = ('userid','username','address','email','mobile','coursetype','courseid','coursename','description','amount',)
    search_fields = ('userid','username','address','email','mobile','coursetype','courseid','coursename','description','amount',)
admin.site.register(buys, buysshow)