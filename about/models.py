from django.db import models

class aboutAdmin(models.Model):
    
    title_page = models.CharField(max_length=500,verbose_name="تیتر صفحه")
    pic = models.ImageField(upload_to='contact/photos/%y/%m/%d/',verbose_name="عکس بالای صفحه")
    title_text = models.CharField(max_length=500,verbose_name="تیتر توضیحات شرکت")
    text_about = models.TextField(blank=True,verbose_name="توضیحات شرکت")
    modir1_pic=models.ImageField(upload_to='about/photos/%y/%m/%d/',verbose_name="عکس مدیر 1")
    modir1_semat=models.CharField(max_length=300,verbose_name="سمت مدیر 1")
    modir1_name=models.CharField(max_length=300,verbose_name="نام و نام خانوادگی مدیر 1")
    modir1_text=models.TextField(verbose_name="توضیحات درباره مدیر 1")
    modir1_email=models.EmailField(max_length=300,verbose_name="ایمیل مدیر 1")
    modir2_pic=models.ImageField(upload_to='about/photos/%y/%m/%d/',verbose_name="عکس مدیر 2")
    modir2_semat=models.CharField(max_length=300,verbose_name="سمت مدیر 2")
    modir2_name=models.CharField(max_length=300,verbose_name="نام و نام خانوادگی مدیر 2")
    modir2_text=models.TextField(verbose_name="توضیحات درباره مدیر 2")
    modir2_email=models.EmailField(max_length=300,verbose_name="ایمیل مدیر 2")
    modir3_pic=models.ImageField(upload_to='about/photos/%y/%m/%d/',verbose_name="عکس مدیر 3")
    modir3_semat=models.CharField(max_length=300,verbose_name="سمت مدیر 3")
    modir3_name=models.CharField(max_length=300,verbose_name="نام و نام خانوادگی مدیر 3")
    modir3_text=models.TextField(verbose_name="توضیحات درباره مدیر 3")
    modir3_email=models.EmailField(max_length=300,verbose_name="ایمیل مدیر 3")
    pic_is_publish=models.BooleanField(default=True,verbose_name="نمایش یا عدم نمایش عکس های محیط شرکت")
    pic_title=models.CharField(max_length=500,verbose_name="تیتر عکس های محیط شرکت")
    pic1=models.ImageField(upload_to='about/photos/%y/%m/%d/',verbose_name="عکس شماره 1")
    pic2=models.ImageField(upload_to='about/photos/%y/%m/%d/',verbose_name="عکس شماره 2")
    pic3=models.ImageField(upload_to='about/photos/%y/%m/%d/',verbose_name="عکس شماره 3")
    pic4=models.ImageField(upload_to='about/photos/%y/%m/%d/',verbose_name="عکس شماره 4")
    pic5=models.ImageField(upload_to='about/photos/%y/%m/%d/',verbose_name="عکس شماره 5")
    pic6=models.ImageField(upload_to='about/photos/%y/%m/%d/',verbose_name="عکس شماره 6")
    pic7=models.ImageField(upload_to='about/photos/%y/%m/%d/',verbose_name="عکس شماره 7")
    pic8=models.ImageField(upload_to='about/photos/%y/%m/%d/',verbose_name="عکس شماره 8")
    def __str__(self):
        return self.title_page
    class Meta:
        verbose_name_plural="تنظیمات صفحه درباره ما"