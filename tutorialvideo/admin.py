from django.contrib import admin
from .models import tutorialvideoAdmin,coursevideo2 , videos


class tutorialvideoAdminshow(admin.ModelAdmin):
    list_display = ('title_page', 'title_search','text_click')
admin.site.register(tutorialvideoAdmin, tutorialvideoAdminshow)



class coursevideo2show(admin.ModelAdmin):
    list_display = ('coursename','modaresinfkey','reshteTahsilifkey','hazine','saattadris',)
    list_filter = ('modaresinfkey','maghtafkey','reshteTahsilifkey',)
    search_fields = ('coursename',)
admin.site.register(coursevideo2, coursevideo2show)



class videosshow(admin.ModelAdmin):
    list_display = ('videoname','coursenamefkey','videolink_is_published','videofile_is_published',)
    list_filter = ('coursenamefkey',)
    search_fields = ('videoname',)
    list_per_page = 10
admin.site.register(videos, videosshow)