from django.db import models
from ckeditor.fields import RichTextField


class galerysAdmin(models.Model):
    
    title_page = models.CharField(max_length=500,verbose_name="تیتر صفحه")
    pic = models.ImageField(upload_to='classlinks/photos/%y/%m/%d/',verbose_name="عکس بالای صفحه")
    title_news = models.CharField(max_length=500,verbose_name="تیتر عکس های گالری")
    
    
    def __str__(self):
        return self.title_page
    class Meta:
        verbose_name_plural="تنظیمات صفحه گالری"


class galerys(models.Model):
    title = models.CharField(max_length=3000,verbose_name="تیتر عکس")
    about = RichTextField(verbose_name="توضیحات عکس")
    pic = models.ImageField(upload_to='news/photos/%y/%m/%d/',verbose_name="عکس")
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural="عکس ها"




