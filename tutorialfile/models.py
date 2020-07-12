from django.db import models
from pages.models import maghtaTahsili, modaresin, reshteTahsili

class tutorialfileAdmin(models.Model):
    
    title_page = models.CharField(max_length=500,verbose_name="تیتر صفحه")
    pic = models.ImageField(upload_to='tutorialfile/photos/%y/%m/%d/',verbose_name="عکس بالای صفحه")
    title_search = models.CharField(max_length=500,verbose_name="تیتر قسمت سرچ")
    text_click =  models.CharField(max_length=500,verbose_name="تیتر دکمه سرچ")
    title_1 = models.CharField(max_length=500,verbose_name="تیتر اول، فایل های پیشنهادی")
    title_2 = models.CharField(max_length=500,verbose_name="تیتر دوم، جدیدترین فایل ها")
    
    def __str__(self):
        return self.title_page
    class Meta:
        verbose_name_plural="تنظیمات صفحه"




class coursefile2(models.Model):
    
    maghtafkey = models.ForeignKey(maghtaTahsili, on_delete=models.DO_NOTHING,verbose_name="مقطع")
    reshteTahsilifkey = models.ForeignKey(reshteTahsili, on_delete=models.DO_NOTHING,verbose_name="رشته")
    modaresinfkey = models.ForeignKey(modaresin, on_delete=models.DO_NOTHING,verbose_name="نام استاد")
    pic = models.ImageField(upload_to='coursefile/photos/%y/%m/%d/',verbose_name="فایل عکس")
    coursename = models.CharField(max_length=1000,verbose_name="نام درس")
    saattadris = models.CharField(max_length=1000,verbose_name="زمان درس")
    tozihat = models.TextField(verbose_name="توضیحات")
    hazine = models.IntegerField(verbose_name="هزینه به ریال")
    
    def __str__(self):
        return self.coursename
    class Meta:
        verbose_name_plural="درس ها"
    


class files(models.Model):
    
    coursenamefkey = models.ForeignKey(coursefile2, on_delete=models.DO_NOTHING,verbose_name="نام درس")
    filename = models.CharField(max_length=1000,verbose_name="نام فایل")
    filelink_is_published = models.BooleanField(default=True,verbose_name="پابلیش لینک فایل")
    filelink = models.CharField(max_length=1000 ,blank=True,verbose_name="لینک فایل")
    filefile_is_published = models.BooleanField(default=True,verbose_name="پابلیش فایل")
    filefile = models.FileField(upload_to='coursefile/files/%y/%m/%d/',blank=True,verbose_name="فایل")
    
    
    def __str__(self):
        return self.filename
    class Meta:
        verbose_name_plural="فایل ها"