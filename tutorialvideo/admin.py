from django.contrib import admin
from .models import tutorialvideoAdmin,coursevideo2


class tutorialvideoAdminshow(admin.ModelAdmin):
    list_display = ('title_page', 'title_search','text_click')
   
    


admin.site.register(tutorialvideoAdmin, tutorialvideoAdminshow)


class coursevideo2show(admin.ModelAdmin):
    list_display = ('coursename',)
   
    


admin.site.register(coursevideo2, coursevideo2show)