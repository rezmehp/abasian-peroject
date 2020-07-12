from django.db import models





class karbaruser1(models.Model):
    username = models.CharField(max_length=200,verbose_name="نام کاربری")
    first_name = models.CharField(max_length=200,verbose_name="نام")
    last_name = models.CharField(max_length=200,verbose_name="نام خانوادگی")
    tell = models.IntegerField(verbose_name="موبایل")
    melli_code = models.IntegerField(verbose_name="کد ملی")
    password = models.CharField(max_length=200,verbose_name="پسورد")
    gender = models.CharField(max_length=200,verbose_name="جنسیت")
    email = models.EmailField(max_length=200,verbose_name="ایمیل")
    maghta = models.CharField(max_length=200,verbose_name="مقطع تحصیلی")
    reshte = models.CharField(max_length=200,verbose_name="رشته تحصیلی")
    shahr = models.CharField(max_length=200,verbose_name="شهر")
    ostan = models.CharField(max_length=200,verbose_name="استان")

    def __str__(self):
        return self.username+" "+self.maghta+" "+self.reshte
    class Meta:
        verbose_name_plural="تنظیمات کاربران"