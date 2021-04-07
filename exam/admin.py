from django.contrib import admin
from .models import tutorialexamAdmin,courseexam2 , exams2 ,UserAnswerTest, examsanswer2


class tutorialexamAdminshow(admin.ModelAdmin):
    list_display = ('title_page', 'title_search','text_click')
admin.site.register(tutorialexamAdmin, tutorialexamAdminshow)


class examsanswer2show(admin.ModelAdmin):
    list_display = ('coursequestionfkey','examanswer_number','examanswer')
    search_fields = ('examanswer',)
admin.site.register(examsanswer2, examsanswer2show)




class courseexam2show(admin.ModelAdmin):
    list_display = ('coursename','hazine','hazineoff','off_is_published','saattadris',)
    search_fields = ('coursename',)
    list_editable = ('off_is_published',)
admin.site.register(courseexam2, courseexam2show)



class exams2show(admin.ModelAdmin):
    list_display = ('examquestion','coursenamefkey','examquestion_published',)
    list_per_page = 10 
    list_filter = ('coursenamefkey','examquestion_published',)
    search_fields = ('examquestion',)
    
admin.site.register(exams2, exams2show)




class UserAnswerTestshow(admin.ModelAdmin):
    list_display = ('usernamefkey','courseexamfkey','examquestionfkey','userexamanswer',)
admin.site.register(UserAnswerTest, UserAnswerTestshow)