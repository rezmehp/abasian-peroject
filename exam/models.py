from django.db import models
from django.contrib.auth.models import User
from pages.models import maghtaTahsili, modaresin, reshteTahsili

class tutorialexamAdmin(models.Model):
    
    title_page = models.CharField(max_length=500,verbose_name="تیتر صفحه")
    pic = models.ImageField(upload_to='tutorialexam/photos/%y/%m/%d/',verbose_name="عکسر بالای صفحه")
    title_search = models.CharField(max_length=500,verbose_name="تیتر سرچ")
    text_click =  models.CharField(max_length=500,verbose_name="تیتر کلیک سرچ")
    title_1 = models.CharField(max_length=500,verbose_name="تیتر آزمون های مرتبط")
    title_2 = models.CharField(max_length=500,verbose_name="تیتر جدیدترین آزمون ها")
    
    def __str__(self):
        return self.title_page
    class Meta:
        verbose_name_plural="تنظیمات صفحه آزمون"



class courseexam2(models.Model):
    
    maghtafkey = models.ForeignKey(maghtaTahsili, on_delete=models.DO_NOTHING,verbose_name="انتخاب مقطع تحصیلی")
    reshteTahsilifkey = models.ForeignKey(reshteTahsili, on_delete=models.DO_NOTHING,verbose_name="انتخاب رشته تحصیلی")
    modaresinfkey = models.ForeignKey(modaresin, on_delete=models.DO_NOTHING,verbose_name="انتخاب مدرس")
    pic = models.ImageField(upload_to='courseexam/photos/%y/%m/%d/',verbose_name="عکس")
    coursename = models.CharField(max_length=1000,verbose_name="نام آزمون")
    saattadris = models.CharField(max_length=1000,verbose_name="مدت آزمون به دقیقه")
    tozihat = models.TextField(verbose_name="توضیحات")
    hazine = models.IntegerField(verbose_name="هزینه به ریال")
    
    def __str__(self):
        return self.coursename
    class Meta:
        verbose_name_plural="ثبت آزمون"

class exams(models.Model):
    
    coursenamefkey = models.ForeignKey(courseexam2, on_delete=models.DO_NOTHING,verbose_name="انتخاب آزمون")
   
    examquestion_published = models.BooleanField(default=True,verbose_name="نمایش یا عدم نمایش سوال")
    examquestion = models.TextField(max_length=50000,verbose_name="متن سوال")
    
    
    examanswer1_true = models.BooleanField(default=False)
    examanswer1 = models.TextField(max_length=50001)
    examanswer2_true = models.BooleanField(default=False)
    examanswer2 = models.TextField(max_length=50000)
    examanswer3_true = models.BooleanField(default=False)
    examanswer3 = models.TextField(max_length=50000)
    examanswer4_true = models.BooleanField(default=False)
    examanswer4 = models.TextField(max_length=50000)
    

    examtext_published = models.BooleanField(default=False)
    examtext = models.TextField(max_length=50000, blank=True)
    examfiletext_published = models.BooleanField(default=False)
    examfiletext = models.FileField(upload_to='courseexam/exams/%y/%m/%d/',blank=True)


    examlinkpic_published = models.BooleanField(default=False)
    examlinkpic = models.TextField(max_length=2000 ,blank=True)
    examfilepic_published = models.BooleanField(default=False)
    examfilepic = models.FileField(upload_to='courseexam/exams/%y/%m/%d/',blank=True)

    
    examlinkvideo_published = models.BooleanField(default=False)
    examlinkvideo = models.TextField(max_length=2000 ,blank=True)
    examfilevideo_published = models.BooleanField(default=False)
    examfilevideo = models.FileField(upload_to='courseexam/exams/%y/%m/%d/',blank=True)

    
    examlinkaudio_published = models.BooleanField(default=False)
    examlinkaudio = models.TextField(max_length=2000 ,blank=True)
    examfileaudio_published = models.BooleanField(default=False)
    examfileaudio = models.FileField(upload_to='courseexam/exams/%y/%m/%d/',blank=True)
    
  
    examanswer_published = models.BooleanField(default=False)
    examanswer = models.TextField(max_length=50000, blank=True)  
    examfileanswer_published = models.BooleanField(default=False)
    examfileanswer = models.FileField(upload_to='courseexam/exams/%y/%m/%d/',blank=True)

    def __str__(self):
        return self.examquestion



class exams2(models.Model):
    
    coursenamefkey = models.ForeignKey(courseexam2, on_delete=models.DO_NOTHING,verbose_name="انتخاب آزمون")
   
    examquestion_published = models.BooleanField(default=True,verbose_name="نمایش یا عدم نمایش سوال")
    examquestion = models.TextField(max_length=50000,verbose_name="متن سوال")
    
    
    examanswer1 = models.TextField(max_length=50001,verbose_name="گزینه 1")
    examanswer2 = models.TextField(max_length=50000,verbose_name="گزینه 2")
    examanswer3 = models.TextField(max_length=50000,verbose_name="گزینه 3")
    examanswer4 = models.TextField(max_length=50000,verbose_name="گزینه 4")
    trueanswer = models.TextField(max_length=1,verbose_name="شماره گزینه صحیح از 1 تا 4")


    examtext_published = models.BooleanField(default=False,verbose_name="نمایش یا عدم نمایش متن برای سوال")
    examtext = models.TextField(max_length=50000, blank=True,verbose_name="متن توضیحات برای سوال")
    examfiletext_published = models.BooleanField(default=False,verbose_name="نمایش یا عدم نمایش فایل متن برای سوال")
    examfiletext = models.FileField(upload_to='courseexam/exams/%y/%m/%d/',blank=True,verbose_name="فایل متن توضیحات برای سوال")


    examlinkpic_published = models.BooleanField(default=False,verbose_name="نمایش یا عدم نمایش لینک عکس برای سوال")
    examlinkpic = models.TextField(max_length=2000 ,blank=True,verbose_name="لینک عکس توضیحات برای سوال")
    examfilepic_published = models.BooleanField(default=False,verbose_name="نمایش یا عدم نمایش فایل عکس برای سوال")
    examfilepic = models.FileField(upload_to='courseexam/exams/%y/%m/%d/',blank=True,verbose_name="فایل عکس توضیحات برای سوال")

    
    examlinkvideo_published = models.BooleanField(default=False,verbose_name="نمایش یا عدم نمایش لینک ویدئو برای سوال")
    examlinkvideo = models.TextField(max_length=2000 ,blank=True,verbose_name="لینک ویدئو توضیحات برای سوال")
    examfilevideo_published = models.BooleanField(default=False,verbose_name="نمایش یا عدم نمایش فایل ویدئو برای سوال")
    examfilevideo = models.FileField(upload_to='courseexam/exams/%y/%m/%d/',blank=True,verbose_name="فایل ویدئو توضیحات برای سوال")

    
    examlinkaudio_published = models.BooleanField(default=False,verbose_name="نمایش یا عدم نمایش لینک صوت برای سوال")
    examlinkaudio = models.TextField(max_length=2000 ,blank=True,verbose_name="لینک صوت توضیحات برای سوال")
    examfileaudio_published = models.BooleanField(default=False,verbose_name="نمایش یا عدم نمایش فایل صوت برای سوال")
    examfileaudio = models.FileField(upload_to='courseexam/exams/%y/%m/%d/',blank=True,verbose_name="فایل صوت توضیحات برای سوال")
    
  
    examanswer_published = models.BooleanField(default=False,verbose_name="نمایش یا عدم نمایش متن جواب سوال")
    examanswer = models.TextField(max_length=50000, blank=True,verbose_name="متن جواب برای سوال")  
    examfileanswer_published = models.BooleanField(default=False,verbose_name="نمایش یا عدم نمایش فایل جواب سوال")
    examfileanswer = models.FileField(upload_to='courseexam/exams/%y/%m/%d/',blank=True,verbose_name="فایل متن توضیحات برای سوال")

    def __str__(self):
        return self.examquestion
    class Meta:
        verbose_name_plural="ثبت سوالات آزمون"





class UserAnswerTest(models.Model):
    
    courseexamfkey = models.TextField(verbose_name="آیدی درس")
    usernamefkey = models.TextField(verbose_name="آیدی کاربر")
    examquestionfkey = models.TextField(verbose_name="آیدی سوال")
    userexamanswer = models.TextField(verbose_name="جواب کاربر")
    
    def __str__(self):
        return self.userexamanswer
    class Meta:
        verbose_name_plural="جواب کاربر به سوال"
    