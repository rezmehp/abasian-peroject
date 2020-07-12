from django.db import models

class footerAdmin(models.Model):
    title = models.CharField(max_length=2000,verbose_name="تیتر فوتر صفحات")
    twitter = models.CharField(max_length=2000,verbose_name="لینک توئیتر")
    twitter_published = models.BooleanField(default=True,verbose_name="نمایش یا عدم نمایش توئیتر")
    linkedin = models.CharField(max_length=2000,verbose_name="لینک لینک این")
    linkedin_published = models.BooleanField(default=True,verbose_name="نمایش یا عدم نمایش لینک این")
    instagram = models.CharField(max_length=2000,verbose_name="لینک اینستاگرام")
    instagram_published = models.BooleanField(default=True,verbose_name="نمایش یا عدم نمایش اینستاگرام")
    mail = models.CharField(max_length=2000,verbose_name="لینک ایمیل")
    mail_published = models.BooleanField(default=True,verbose_name="نمایش یا عدم نمایش ایمیل")
    whatsapp = models.CharField(max_length=2000,verbose_name="لینک واتس اپ")
    whatsapp_published = models.BooleanField(default=True,verbose_name="نمایش یا عدم نمایش واتس اپ")
    telegram = models.CharField(max_length=2000,verbose_name="لینک تلگرام")
    telegram_published = models.BooleanField(default=True,verbose_name="نمایش یا عدم نمایش تلگرام")
    

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural="تنظیمات فوتر صفحات"


class sliderImage(models.Model):
    pic = models.ImageField(upload_to='slider/photos/%y/%m/%d/',verbose_name="عکس های اسلایدر صفحه اول")

    class Meta:
        verbose_name_plural="به روز رسانی عکس های اسلایدر صفحه اول سایت"


class ostanha(models.Model):
    ostanName = models.CharField(max_length=100,verbose_name="نام استان")
    def __str__(self):
        return self.ostanName
    class Meta:
        verbose_name_plural="ثبت استان"


class shahrha(models.Model):
    ostanNamefkey = models.ForeignKey(ostanha, on_delete=models.DO_NOTHING,verbose_name="انتخاب استان")
    shahrNames = models.CharField(max_length=100,verbose_name="نام شهر")
    def __str__(self):
        return self.shahrNames
    class Meta:
        verbose_name_plural="ثبت شهر"

        

class maghtaTahsili(models.Model):
    maghta = models.CharField(max_length=100,verbose_name="نام مقطع تحصیلی")
    def __str__(self):
        return self.maghta
    class Meta:
        verbose_name_plural="ثبت مقطع"


class reshteTahsili(models.Model):
    maghtafkey = models.ForeignKey(maghtaTahsili, on_delete=models.DO_NOTHING,verbose_name="انتخاب مقطع تحصیلی")
    reshte = models.CharField(max_length=100,verbose_name="نام رشته")
    def __str__(self):
        return self.reshte
    class Meta:
        verbose_name_plural="ثبت رشته"

class modaresin(models.Model):
    modares = models.CharField(max_length=300,verbose_name="نام و نام خانوادگی مدرس")
    email_modares = models.CharField(max_length=2000,verbose_name="ایمیل مدرس")
    def __str__(self):
        return self.modares
    class Meta:
        verbose_name_plural="ثبت مدرسین"