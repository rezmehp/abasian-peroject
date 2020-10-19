from django.db import models
from pages.models import maghtaTahsili, modaresin, reshteTahsili
from ckeditor.fields import RichTextField

class tutorialvideoAdmin(models.Model):
    
    title_page = models.CharField(max_length=500,verbose_name="تیتر صفحه")
    pic = models.ImageField(upload_to='tutorialvideo/photos/%y/%m/%d/',verbose_name="عکس بالای صفحه")
    title_search = models.CharField(max_length=500,verbose_name="تیتر قسمت سرچ")
    text_click =  models.CharField(max_length=500,verbose_name="تیتر دکمه سرچ")
    title_1 = models.CharField(max_length=500,verbose_name="تیتر اول، ویدیوهای پیشنهادی")
    title_2 = models.CharField(max_length=500,verbose_name="تیتر دوم، جدیدترین ویدیوها")
    
    def __str__(self):
        return self.title_page
    class Meta:
        verbose_name_plural="تنظیمات صفحه"



class coursevideo2(models.Model):
    
    maghtafkey = models.ForeignKey(maghtaTahsili, on_delete=models.DO_NOTHING,verbose_name="مقطع")
    reshteTahsilifkey = models.ForeignKey(reshteTahsili, on_delete=models.DO_NOTHING,verbose_name="رشته")
    modaresinfkey = models.ForeignKey(modaresin, on_delete=models.DO_NOTHING,verbose_name="نام استاد")
    pic = models.ImageField(upload_to='coursevideo/photos/%y/%m/%d/',verbose_name="فایل عکس")
    coursename = models.CharField(max_length=1000,verbose_name="نام درس")
    saattadris = models.CharField(max_length=1000,verbose_name="زمان درس")
    tozihat = RichTextField(verbose_name="توضیحات")
    tizer = models.CharField(max_length=1000,verbose_name="لینک فایل تیزر")
    tizer_is_published = models.BooleanField(default=True,verbose_name="نمایش فایل تیزر")
    hazine = models.IntegerField(verbose_name="هزینه به تومان")
    
    def __str__(self):
        return self.coursename
    class Meta:
        verbose_name_plural="درس ها"
        
class videos(models.Model):
    
    coursenamefkey = models.ForeignKey(coursevideo2, on_delete=models.DO_NOTHING,verbose_name="نام درس")
    videoname = models.CharField(max_length=1000,verbose_name="نام ویدیو")
    videolink_is_published = models.BooleanField(default=True,verbose_name="پابلیش لینک ویدیو")
    videolink = models.CharField(max_length=1000 ,blank=True,verbose_name="لینک ویدیو")
    videofile_is_published = models.BooleanField(default=True,verbose_name="پابلیش فایل ویدیو")
    videofile = models.FileField(upload_to='coursevideo/videos/%y/%m/%d/',blank=True,verbose_name="فایل ویدیو")
    
    
    def __str__(self):
        return self.videoname
    class Meta:
        verbose_name_plural="ویدیو ها"