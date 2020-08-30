from django.db import models


class buys(models.Model):
    userid = models.CharField(max_length=5000,verbose_name="آیدی کاربر")
    username = models.CharField(max_length=5000,verbose_name="نام کاربری")
    address = models.CharField(max_length=5000,verbose_name="آدرس")
    email = models.CharField(max_length=5000,verbose_name="ایمیل")
    mobile = models.CharField(max_length=5000,verbose_name="موبایل")
    coursetype  = models.CharField(max_length=5000,verbose_name="نوع درس")
    courseid = models.CharField(max_length=5000,verbose_name="آیدی درس")
    coursename = models.CharField(max_length=5000,verbose_name="نام درس")
    description = models.CharField(max_length=5000,verbose_name="توضیحات فروش ")
    amount = models.CharField(max_length=5000,verbose_name="هزینه")

    
    def __str__(self):
        return self.description
    class Meta:
        verbose_name_plural="خرید ها"