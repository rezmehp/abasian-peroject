from django.db import models
from django.contrib.auth.models import User
from accounts.models import karbaruser1
from datetime import datetime
from ckeditor.fields import RichTextField

class contactAdmin(models.Model):
    title_page = models.CharField(max_length=200,verbose_name="تیتر صفحه")
    pic = models.ImageField(upload_to='contact/photos/%y/%m/%d/',verbose_name="عکس بالای صفحه")
    title_message = models.CharField(max_length=200,verbose_name="تیتر قسمت ارسال پیام")
    click = models.CharField(max_length=30,verbose_name="تیتر کلیک")
    address = models.TextField(blank=True,verbose_name="آدرس نقشه گوگل")
    def __str__(self):
        return self.title_page
    class Meta:
        verbose_name_plural="تنظیمات صفحه تماس با ما"

class contactuserpayam4(models.Model):
    usernamefkey = models.ForeignKey(User, on_delete=models.DO_NOTHING,verbose_name="تیتر صفحه")
    soal = models.TextField(blank=True,verbose_name="سوال کاربر")
    javabadmin = RichTextField(blank=True,verbose_name="جواب ادمین")
       
    def __str__(self):
        return self.usernamefkey 
    class Meta:
        verbose_name_plural="سوالات کاربران و جواب دهی"


class contactuserpm(models.Model):
    usernamefkey = models.ForeignKey(User, on_delete=models.DO_NOTHING,verbose_name="کاربر مورد نظر")
    soal = models.TextField(blank=True,verbose_name="سوال کاربر")
    javabadmin = RichTextField(blank=True,verbose_name="جواب ادمین")
  
    def __str__(self):
        return str(self.usernamefkey) if self.usernamefkey else ''
    class Meta:
        verbose_name_plural="سوالات کاربران و جواب دهی"