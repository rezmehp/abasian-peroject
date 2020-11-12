from django.contrib import admin
from .models import tutorialvoiceAdmin,coursevoice2 , voices ,voicepics


class tutorialvoiceAdminshow(admin.ModelAdmin):
    list_display = ('title_page', 'title_search','text_click')
admin.site.register(tutorialvoiceAdmin, tutorialvoiceAdminshow)



class coursevoice2show(admin.ModelAdmin):
    list_display = ('coursename','modaresinfkey','reshteTahsilifkey','hazine','hazineoff','off_is_published','saattadris',)
    list_filter = ('modaresinfkey','maghtafkey','reshteTahsilifkey',)
    list_editable = ('off_is_published',)
    search_fields = ('coursename',)
admin.site.register(coursevoice2, coursevoice2show)



class voicesshow(admin.ModelAdmin):
    list_display = ('voicename','coursenamefkey','voicelink_is_published','voicefile_is_published',)
    list_filter = ('coursenamefkey',)
    search_fields = ('voicename',)
    list_per_page = 10
admin.site.register(voices, voicesshow)





class voicepicsshow(admin.ModelAdmin):
    list_display = ('voicepicname','coursenamefkey','voicepiclink_is_published','voicepicfile_is_published',)
    list_filter = ('coursenamefkey',)
    search_fields = ('voicepicname',)
    list_per_page = 10
admin.site.register(voicepics, voicepicsshow)