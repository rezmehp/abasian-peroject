from django.contrib import admin
from .models import tutorialexamAdmin,courseexam2 , exams2 ,UserAnswerTest


class tutorialexamAdminshow(admin.ModelAdmin):
    list_display = ('title_page', 'title_search','text_click')
admin.site.register(tutorialexamAdmin, tutorialexamAdminshow)


class courseexam2show(admin.ModelAdmin):
    list_display = ('coursename',)
    search_fields = ('coursename',)
admin.site.register(courseexam2, courseexam2show)



class exams2show(admin.ModelAdmin):
    list_display = ('examquestion',)
    list_filter = ('coursenamefkey',)
    search_fields = ('examquestion',)
admin.site.register(exams2, exams2show)




class UserAnswerTestshow(admin.ModelAdmin):
    list_display = ('usernamefkey','courseexamfkey','examquestionfkey','userexamanswer',)
admin.site.register(UserAnswerTest, UserAnswerTestshow)