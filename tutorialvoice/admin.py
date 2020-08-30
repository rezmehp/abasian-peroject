from django.contrib import admin
from .models import tutorialvoiceAdmin,coursevoice2 , voices


class tutorialvoiceAdminshow(admin.ModelAdmin):
    list_display = ('title_page', 'title_search','text_click')
admin.site.register(tutorialvoiceAdmin, tutorialvoiceAdminshow)



class coursevoice2show(admin.ModelAdmin):
    list_display = ('coursename','modaresinfkey','reshteTahsilifkey','hazine','saattadris',)
    list_filter = ('modaresinfkey','maghtafkey','reshteTahsilifkey',)
    search_fields = ('coursename',)
admin.site.register(coursevoice2, coursevoice2show)



class voicesshow(admin.ModelAdmin):
    list_display = ('voicename','coursenamefkey','voicelink_is_published','voicefile_is_published',)
    list_filter = ('coursenamefkey',)
    search_fields = ('voicename',)
    list_per_page = 10
admin.site.register(voices, voicesshow)