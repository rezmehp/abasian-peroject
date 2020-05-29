from django.db import models
from pages.models import maghtaTahsili, modaresin, reshteTahsili

class tutorialvideoAdmin(models.Model):
    
    title_page = models.CharField(max_length=500)
    pic = models.ImageField(upload_to='tutorialvideo/photos/%y/%m/%d/')
    title_search = models.CharField(max_length=500)
    text_click =  models.CharField(max_length=500)
    title_1 = models.CharField(max_length=500)
    title_2 = models.CharField(max_length=500)
    
    def __str__(self):
        return self.title_page




class coursevideo2(models.Model):
    
    maghtafkey = models.ForeignKey(maghtaTahsili, on_delete=models.DO_NOTHING)
    reshteTahsilifkey = models.ForeignKey(reshteTahsili, on_delete=models.DO_NOTHING)
    modaresinfkey = models.ForeignKey(modaresin, on_delete=models.DO_NOTHING)
    pic = models.ImageField(upload_to='coursevideo/photos/%y/%m/%d/')
    coursename = models.CharField(max_length=1000)
    saattadris = models.CharField(max_length=1000)
    tozihat = models.TextField()
    hazine = models.IntegerField()
    
    def __str__(self):
        return self.coursename


class videos(models.Model):
    
    coursenamefkey = models.ForeignKey(coursevideo2, on_delete=models.DO_NOTHING)
    videoname = models.CharField(max_length=1000)
    videolink_is_published = models.BooleanField(default=True)
    videolink = models.CharField(max_length=1000 ,blank=True)
    videofile_is_published = models.BooleanField(default=True)
    videofile = models.FileField(upload_to='coursevideo/videos/%y/%m/%d/',blank=True)
    
    
    def __str__(self):
        return self.videoname