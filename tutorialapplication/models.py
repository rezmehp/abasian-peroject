from django.db import models
from pages.models import maghtaTahsili, modaresin, reshteTahsili
from ckeditor.fields import RichTextField



class tutorialapplicationAdmin(models.Model):
    
    title_page = models.CharField(max_length=500,verbose_name="تیتر صفحه")
    pic = models.ImageField(upload_to='tutorialapplication/photos/%y/%m/%d/',verbose_name="عکس بالای صفحه")
    title_search = models.CharField(max_length=500,verbose_name="تیتر قسمت سرچ")
    text_click =  models.CharField(max_length=500,verbose_name="تیتر دکمه سرچ")
    title_1 = models.CharField(max_length=500,verbose_name="تیتر اول، فایل های پیشنهادی")
    title_2 = models.CharField(max_length=500,verbose_name="تیتر دوم، جدیدترین فایل ها")
    
    def __str__(self):
        return self.title_page
    class Meta:
        verbose_name_plural="تنظیمات صفحه"



class courseapplication2(models.Model):
    
    maghtafkey = models.ForeignKey(maghtaTahsili, on_delete=models.DO_NOTHING,verbose_name="مقطع")
    reshteTahsilifkey = models.ForeignKey(reshteTahsili, on_delete=models.DO_NOTHING,verbose_name="رشته")
    modaresinfkey = models.ForeignKey(modaresin, on_delete=models.DO_NOTHING,verbose_name="نام سازنده")
    pic = models.ImageField(upload_to='courseapplication/photos/%y/%m/%d/',verbose_name="فایل عکس")
    coursename = models.CharField(max_length=1000,verbose_name="نام نرم افزار")
    saattadris = models.CharField(max_length=1000,verbose_name="زمان نزم افزار")
    tozihat = RichTextField(verbose_name="توضیحات")
    hazine = models.IntegerField(verbose_name="هزینه به تومان")
    
    def __str__(self):
        return self.coursename
    class Meta:
        verbose_name_plural="نرم افزارها"



class applications(models.Model):
    
    coursenamefkey = models.ForeignKey(courseapplication2, on_delete=models.DO_NOTHING,verbose_name="نام نرم افزار")
    applicationname = models.CharField(max_length=1000,verbose_name="نام فایل")
    applicationlink_is_published = models.BooleanField(default=True,verbose_name="پابلیش لینک فایل")
    applicationlink = models.CharField(max_length=1000 ,blank=True,verbose_name="لینک فایل")
    applicationapplication_is_published = models.BooleanField(default=True,verbose_name="پابلیش فایل")
    applicationapplication = models.FileField(upload_to='courseapplication/applications/%y/%m/%d/',blank=True,verbose_name="فایل")
    
    
    def __str__(self):
        return self.applicationname
    class Meta:
        verbose_name_plural="فایل ها"



class applicationpics(models.Model):
    
    coursenamefkey = models.ForeignKey(courseapplication2, on_delete=models.DO_NOTHING,verbose_name="نام درس")
    applicationpicname = models.CharField(max_length=1000,verbose_name="نام عکس")
    applicationpiclink_is_published = models.BooleanField(default=True,verbose_name="پابلیش لینک عکس")
    applicationpiclink = models.CharField(max_length=1000 ,blank=True,verbose_name="لینک عکس")
    applicationpicfile_is_published = models.BooleanField(default=True,verbose_name="پابلیش فایل عکس")
    applicationpicfile = models.FileField(upload_to='courseapplication/applications/%y/%m/%d/',blank=True,verbose_name="فایل عکس")
    
    
    def __str__(self):
        return self.applicationpicname
    class Meta:
        verbose_name_plural="عکس های محصول"