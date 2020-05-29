from django.db import models
from pages.models import maghtaTahsili, modaresin, reshteTahsili

class tutorialfileAdmin(models.Model):
    
    title_page = models.CharField(max_length=500)
    pic = models.ImageField(upload_to='tutorialfile/photos/%y/%m/%d/')
    title_search = models.CharField(max_length=500)
    text_click =  models.CharField(max_length=500)
    title_1 = models.CharField(max_length=500)
    title_2 = models.CharField(max_length=500)
    
    def __str__(self):
        return self.title_page




class coursefile2(models.Model):
    
    maghtafkey = models.ForeignKey(maghtaTahsili, on_delete=models.DO_NOTHING)
    reshteTahsilifkey = models.ForeignKey(reshteTahsili, on_delete=models.DO_NOTHING)
    modaresinfkey = models.ForeignKey(modaresin, on_delete=models.DO_NOTHING)
    pic = models.ImageField(upload_to='coursefile/photos/%y/%m/%d/')
    coursename = models.CharField(max_length=1000)
    saattadris = models.CharField(max_length=1000)
    tozihat = models.TextField()
    hazine = models.IntegerField()
    
    def __str__(self):
        return self.coursename


class files(models.Model):
    
    coursenamefkey = models.ForeignKey(coursefile2, on_delete=models.DO_NOTHING)
    filename = models.CharField(max_length=1000)
    filelink_is_published = models.BooleanField(default=True)
    filelink = models.CharField(max_length=1000 ,blank=True)
    filefile_is_published = models.BooleanField(default=True)
    filefile = models.FileField(upload_to='coursefile/files/%y/%m/%d/',blank=True)
    
    
    def __str__(self):
        return self.filename