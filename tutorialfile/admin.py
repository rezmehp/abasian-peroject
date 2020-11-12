from django.contrib import admin
from .models import tutorialfileAdmin,coursefile2 , files,filepics


class tutorialfileAdminshow(admin.ModelAdmin):
    list_display = ('title_page', 'title_search','text_click')
admin.site.register(tutorialfileAdmin, tutorialfileAdminshow)


class coursefile2show(admin.ModelAdmin):
    list_display = ('coursename','modaresinfkey','reshteTahsilifkey','hazine','hazineoff','off_is_published','saattadris',)
    list_filter = ('modaresinfkey','maghtafkey','reshteTahsilifkey',)
    search_fields = ('coursename',)
    list_per_page = 10

admin.site.register(coursefile2, coursefile2show)



class filesshow(admin.ModelAdmin):
    list_display = ('filename','coursenamefkey','filelink_is_published','filefile_is_published',)
    list_filter = ('coursenamefkey',)
    search_fields = ('filename',)
    list_per_page = 10

admin.site.register(files, filesshow)




class filepicsshow(admin.ModelAdmin):
    list_display = ('filepicname','coursenamefkey','filepiclink_is_published','filepicfile_is_published',)
    list_filter = ('coursenamefkey',)
    search_fields = ('filepicname',)
    list_per_page = 10
admin.site.register(filepics, filepicsshow)