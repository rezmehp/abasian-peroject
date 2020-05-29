from django.contrib import admin
from .models import tutorialfileAdmin,coursefile2 , files


class tutorialfileAdminshow(admin.ModelAdmin):
    list_display = ('title_page', 'title_search','text_click')
admin.site.register(tutorialfileAdmin, tutorialfileAdminshow)


class coursefile2show(admin.ModelAdmin):
    list_display = ('coursename',)
    search_fields = ('coursename',)
admin.site.register(coursefile2, coursefile2show)



class filesshow(admin.ModelAdmin):
    list_display = ('filename',)
    list_filter = ('coursenamefkey',)
    search_fields = ('filename',)
admin.site.register(files, filesshow)