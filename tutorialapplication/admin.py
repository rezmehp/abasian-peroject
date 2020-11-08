from django.contrib import admin
from .models import tutorialapplicationAdmin,courseapplication2 , applications,applicationpics


class tutorialapplicationAdminshow(admin.ModelAdmin):
    list_display = ('title_page', 'title_search','text_click')
admin.site.register(tutorialapplicationAdmin, tutorialapplicationAdminshow)


class courseapplication2show(admin.ModelAdmin):
    list_display = ('coursename','modaresinfkey','reshteTahsilifkey','hazine','saattadris',)
    list_filter = ('modaresinfkey','maghtafkey','reshteTahsilifkey',)
    search_fields = ('coursename',)
admin.site.register(courseapplication2, courseapplication2show)



class applicationsshow(admin.ModelAdmin):
    list_display = ('applicationname','coursenamefkey','applicationlink_is_published','applicationapplication_is_published',)
    list_filter = ('coursenamefkey',)
    search_fields = ('applicationname',)
admin.site.register(applications, applicationsshow)




class applicationpicsshow(admin.ModelAdmin):
    list_display = ('applicationpicname','coursenamefkey','applicationpiclink_is_published','applicationpicfile_is_published',)
    list_filter = ('coursenamefkey',)
    search_fields = ('applicationpicname',)
    list_per_page = 10
admin.site.register(applicationpics, applicationpicsshow)