from django.contrib import admin
from .models import tutorialapplicationAdmin,courseapplication2 , applications


class tutorialapplicationAdminshow(admin.ModelAdmin):
    list_display = ('title_page', 'title_search','text_click')
admin.site.register(tutorialapplicationAdmin, tutorialapplicationAdminshow)


class courseapplication2show(admin.ModelAdmin):
    list_display = ('coursename','modaresinfkey','reshteTahsilifkey','hazine','saattadris',)
    list_filter = ('modaresinfkey','maghtafkey','reshteTahsilifkey',)
    search_fields = ('coursename',)
admin.site.register(courseapplication2, courseapplication2show)



class applicationsshow(admin.ModelAdmin):
    list_display = ('applicationname',)
    list_filter = ('coursenamefkey',)
    search_fields = ('applicationname',)
admin.site.register(applications, applicationsshow)