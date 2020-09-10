from django.db import models
from ckeditor.fields import RichTextField

class newsAdmin(models.Model):
    
    title_page = models.CharField(max_length=500,verbose_name="تیتر صفحه")
    pic = models.ImageField(upload_to='classlinks/photos/%y/%m/%d/',verbose_name="عکس بالای صفحه")
    title_news = models.CharField(max_length=500,verbose_name="تیتر اخبار")
    
    
    def __str__(self):
        return self.title_page
    class Meta:
        verbose_name_plural="تنظیمات صفحه اخبار"


class news(models.Model):
    title = models.CharField(max_length=3000,verbose_name="تیتر خبر")
    about = RichTextField(verbose_name="توضیحات خبر")
    pic = models.ImageField(upload_to='news/photos/%y/%m/%d/',verbose_name="عکس خبر")
    time = models.TimeField(verbose_name="ساعت انتشار خبر")
    date = models.DateField(verbose_name="تاریخ انتشار خبر")
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural="اخبار"




