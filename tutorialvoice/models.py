from django.db import models
from pages.models import maghtaTahsili, modaresin, reshteTahsili
from ckeditor.fields import RichTextField


class tutorialvoiceAdmin(models.Model):
    
    title_page = models.CharField(max_length=500,verbose_name="تیتر صفحه")
    pic = models.ImageField(upload_to='tutorialvoice/photos/%y/%m/%d/',verbose_name="عکس بالای صفحه")
    title_search = models.CharField(max_length=500,verbose_name="تیتر قسمت سرچ")
    text_click =  models.CharField(max_length=500,verbose_name="تیتر دکمه سرچ")
    title_1 = models.CharField(max_length=500,verbose_name="تیتر اول، صوتهای پیشنهادی")
    title_2 = models.CharField(max_length=500,verbose_name="تیتر دوم، جدیدترین صوتها")
    
    def __str__(self):
        return self.title_page
    class Meta:
        verbose_name_plural="تنظیمات صفحه"



class coursevoice2(models.Model):
    
    maghtafkey = models.ForeignKey(maghtaTahsili, on_delete=models.DO_NOTHING,verbose_name="مقطع")
    reshteTahsilifkey = models.ForeignKey(reshteTahsili, on_delete=models.DO_NOTHING,verbose_name="رشته")
    modaresinfkey = models.ForeignKey(modaresin, on_delete=models.DO_NOTHING,verbose_name="نام استاد")
    pic = models.ImageField(upload_to='coursevoice/photos/%y/%m/%d/',verbose_name="فایل عکس")
    coursename = models.CharField(max_length=1000,verbose_name="نام درس")
    saattadris = models.CharField(max_length=1000,verbose_name="زمان درس")
    tozihat = RichTextField(verbose_name="توضیحات")
    hazine = models.IntegerField(verbose_name="هزینه به تومان")
    
    def __str__(self):
        return self.coursename
    class Meta:
        verbose_name_plural="درس ها"
        
class voices(models.Model):
    
    coursenamefkey = models.ForeignKey(coursevoice2, on_delete=models.DO_NOTHING,verbose_name="نام درس")
    voicename = models.CharField(max_length=1000,verbose_name="نام صوت")
    voicelink_is_published = models.BooleanField(default=True,verbose_name="پابلیش لینک صوت")
    voicelink = models.CharField(max_length=1000 ,blank=True,verbose_name="لینک صوت")
    voicefile_is_published = models.BooleanField(default=True,verbose_name="پابلیش فایل صوت")
    voicefile = models.FileField(upload_to='coursevoice/voices/%y/%m/%d/',blank=True,verbose_name="فایل صوت")
    
    
    def __str__(self):
        return self.voicename
    class Meta:
        verbose_name_plural="صوت ها"