from django.db import models

class linksAdmin(models.Model):
    
    title_page = models.CharField(max_length=500,verbose_name="تیتر صفحه")
    pic = models.ImageField(upload_to='links/photos/%y/%m/%d/',verbose_name="عکس بالای صفحه")
    title_links = models.CharField(max_length=500,verbose_name="تیتر لینک ها")
    
    
    def __str__(self):
        return self.title_page
    class Meta:
        verbose_name_plural="تنظیمات صفحه لینک های مفید"

class allLinks(models.Model):
    link_title = models.CharField(max_length=3000,verbose_name="تیتر لینک")
    link_url = models.CharField(max_length=3000,verbose_name="آدرس لینک ")
    
    def __str__(self):
        return self.link_title
    class Meta:
        verbose_name_plural="لینک ها"