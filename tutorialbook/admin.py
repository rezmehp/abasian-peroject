from django.contrib import admin
from .models import tutorialbookAdmin,coursebook2 , books,bookpics


class tutorialbookAdminshow(admin.ModelAdmin):
    list_display = ('title_page', 'title_search','text_click')
admin.site.register(tutorialbookAdmin, tutorialbookAdminshow)


class coursebook2show(admin.ModelAdmin):
    list_display = ('coursename','modaresinfkey','reshteTahsilifkey','hazine','hazineoff','off_is_published','saattadris',)
    list_filter = ('modaresinfkey','maghtafkey','reshteTahsilifkey',)
    search_fields = ('coursename',)
    list_editable = ('off_is_published',)
admin.site.register(coursebook2, coursebook2show)



class booksshow(admin.ModelAdmin):
    list_display = ('bookname','coursenamefkey','booklink_is_published','bookfile_is_published',)
    list_filter = ('coursenamefkey',)
    search_fields = ('bookname',)
    list_per_page = 10
admin.site.register(books, booksshow)



class bookpicsshow(admin.ModelAdmin):
    list_display = ('bookpicname','coursenamefkey','bookpiclink_is_published','bookpicfile_is_published',)
    list_filter = ('coursenamefkey',)
    search_fields = ('bookpicname',)
    list_per_page = 10
admin.site.register(bookpics, bookpicsshow)