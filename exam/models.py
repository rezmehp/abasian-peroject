from django.db import models
from pages.models import maghtaTahsili, modaresin, reshteTahsili

class tutorialexamAdmin(models.Model):
    
    title_page = models.CharField(max_length=500)
    pic = models.ImageField(upload_to='tutorialexam/photos/%y/%m/%d/')
    title_search = models.CharField(max_length=500)
    text_click =  models.CharField(max_length=500)
    title_1 = models.CharField(max_length=500)
    title_2 = models.CharField(max_length=500)
    
    def __str__(self):
        return self.title_page




class courseexam2(models.Model):
    
    maghtafkey = models.ForeignKey(maghtaTahsili, on_delete=models.DO_NOTHING)
    reshteTahsilifkey = models.ForeignKey(reshteTahsili, on_delete=models.DO_NOTHING)
    modaresinfkey = models.ForeignKey(modaresin, on_delete=models.DO_NOTHING)
    pic = models.ImageField(upload_to='courseexam/photos/%y/%m/%d/')
    coursename = models.CharField(max_length=1000)
    saattadris = models.CharField(max_length=1000)
    tozihat = models.TextField()
    hazine = models.IntegerField()
    
    def __str__(self):
        return self.coursename


class exams(models.Model):
    
    coursenamefkey = models.ForeignKey(courseexam2, on_delete=models.DO_NOTHING)
   
    examquestion_published = models.BooleanField(default=True)
    examquestion = models.TextField(max_length=50000)

    examanswer1_true = models.BooleanField(default=True)
    examanswer1 = models.TextField(max_length=50000)
    examanswer2_true = models.BooleanField(default=True)
    examanswer2 = models.TextField(max_length=50000)
    examanswer3_true = models.BooleanField(default=True)
    examanswer3 = models.TextField(max_length=50000)
    examanswer4_true = models.BooleanField(default=True)
    examanswer4 = models.TextField(max_length=50000)
    


    examtext = models.TextField(max_length=50000, blank=True)
    
    examlinkpic_published = models.BooleanField(default=True)
    examlinkpic = models.TextField(max_length=2000 ,blank=True)
    examfilepic_published = models.BooleanField(default=True)
    examfilepic = models.FileField(upload_to='courseexam/exams/%y/%m/%d/',blank=True)

    
    examlinkvideo_published = models.BooleanField(default=True)
    examlinkvideo = models.TextField(max_length=2000 ,blank=True)
    examfilevideo_published = models.BooleanField(default=True)
    examfilevideo = models.FileField(upload_to='courseexam/exams/%y/%m/%d/',blank=True)

    
    examlinkaudio_published = models.BooleanField(default=True)
    examlinkaudio = models.TextField(max_length=2000 ,blank=True)
    examfileaudio_published = models.BooleanField(default=True)
    examfileaudio = models.FileField(upload_to='courseexam/exams/%y/%m/%d/',blank=True)
    
  
    examanswer_published = models.BooleanField(default=True)
    examanswer = models.TextField(max_length=50000, blank=True)  


    def __str__(self):
        return self.examquestion