from django.db import models
from ckeditor.fields import RichTextField


class classlinksAdmin(models.Model):
    
    title_page = models.CharField(max_length=500,verbose_name="تیتر صفحه")
    pic = models.ImageField(upload_to='classlinks/photos/%y/%m/%d/',verbose_name="عکس بالای صفحه")
    title_classlinks = models.CharField(max_length=500,verbose_name="تیتر لینک کلاس ها")
    
    
    def __str__(self):
        return self.title_page
    class Meta:
        verbose_name_plural="تنظیمات صفحه لینک کلاس های آنلاین"


class allclassLinks3(models.Model):
    link_title = models.CharField(max_length=3000,verbose_name="تیتر کلاس")
    link_about = RichTextField(verbose_name="توضیحات کلاس")
    link_url = models.CharField(max_length=3000,verbose_name="لینک کلاس")
    link_pic = models.ImageField(upload_to='classlinks/photos/%y/%m/%d/',verbose_name="عکس کلاس")
    link_time = models.TimeField(verbose_name="ساعت برگزاری کلاس")
    link_date = models.DateField(verbose_name="تاریخ برگزاری کلاس")
    link_price = models.IntegerField(verbose_name="هزینه کلاس")
    def __str__(self):
        return self.link_title
    class Meta:
        verbose_name_plural="لینک کلاس ها"



class allclassLinks2(models.Model):
    link_title = models.CharField(max_length=3000,verbose_name="تیتر کلاس")
    link_about = models.CharField(max_length=3000,verbose_name="توضیحات کلاس")
    link_url = models.CharField(max_length=3000,verbose_name="لینک کلاس")
    link_pic = models.ImageField(upload_to='classlinks/photos/%y/%m/%d/',verbose_name="عکس کلاس")
    link_time = models.TimeField(verbose_name="ساعت برگزاری کلاس")
    link_date = models.DateField(verbose_name="تاریخ برگزاری کلاس")
    link_price = models.IntegerField(verbose_name="هزینه کلاس")
    def __str__(self):
        return self.link_title
    class Meta:
        verbose_name_plural="لینک کلاس ها"


class allclassLinks1(models.Model):
    link_title = models.CharField(max_length=3000,verbose_name="تیتر کلاس")
    link_about = models.CharField(max_length=3000,verbose_name="توضیحات کلاس")
    link_url = models.CharField(max_length=3000,verbose_name="لینک کلاس")
    link_pic = models.ImageField(upload_to='classlinks/photos/%y/%m/%d/',verbose_name="عکس کلاس")
    link_time = models.TimeField(verbose_name="ساعت برگزاری کلاس")
    link_date = models.TimeField(verbose_name="تاریخ برگزاری کلاس")
    link_price = models.IntegerField(verbose_name="هزینه کلاس")
    def __str__(self):
        return self.link_title
    class Meta:
        verbose_name_plural="لینک کلاس ها"

class allclassLinks(models.Model):
    link_title = models.CharField(max_length=3000,verbose_name="تیتر لینک کلاس")
    link_about = models.CharField(max_length=3000,verbose_name="توضیحات لینک کلاس")
    link_url = models.CharField(max_length=3000,verbose_name="لینک کلاس")
    link_pic = models.ImageField(upload_to='classlinks/photos/%y/%m/%d/',verbose_name="عکس لینک کلاس")
    def __str__(self):
        return self.link_title
    class Meta:
        verbose_name_plural="لینک کلاس ها"