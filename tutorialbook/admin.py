from django.contrib import admin
from .models import tutorialbookAdmin,coursebook2 , books


class tutorialbookAdminshow(admin.ModelAdmin):
    list_display = ('title_page', 'title_search','text_click')
admin.site.register(tutorialbookAdmin, tutorialbookAdminshow)


class coursebook2show(admin.ModelAdmin):
    list_display = ('coursename','modaresinfkey','reshteTahsilifkey','hazine','saattadris',)
    list_filter = ('modaresinfkey','maghtafkey','reshteTahsilifkey',)
    search_fields = ('coursename',)
admin.site.register(coursebook2, coursebook2show)



class booksshow(admin.ModelAdmin):
    list_display = ('bookname',)
    list_filter = ('coursenamefkey',)
    search_fields = ('bookname',)
admin.site.register(books, booksshow)