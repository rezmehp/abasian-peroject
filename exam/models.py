from django.db import models
from django.contrib.auth.models import User
from pages.models import maghtaTahsili, modaresin, reshteTahsili
from ckeditor.fields import RichTextField
from smart_selects.db_fields import ChainedForeignKey

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
    
    maghtafkey = models.ForeignKey(maghtaTahsili, on_delete=models.DO_NOTHING,verbose_name="مقطع")
    reshteTahsilifkey = models.ForeignKey(reshteTahsili, on_delete=models.DO_NOTHING,verbose_name="رشته")
    modaresinfkey = models.ForeignKey(modaresin, on_delete=models.DO_NOTHING,verbose_name="نام استاد")
    pic = models.ImageField(upload_to='courseexam/photos/%y/%m/%d/',verbose_name="عکس")
    coursename = models.CharField(max_length=1000,verbose_name="نام آزمون")
    saattadris = models.CharField(max_length=1000,verbose_name="مدت آزمون به دقیقه")
    tozihat = RichTextField(verbose_name="توضیحات")
    hazine = models.IntegerField(verbose_name="هزینه به تومان")
    off_is_published = models.BooleanField(default=True,verbose_name="تخفیف دارد")
    hazineoff = models.IntegerField(verbose_name="هزینه با تخفیف به تومان")
    
    def __str__(self):
        return self.coursename
    class Meta:
        verbose_name_plural="ثبت آزمون"


class exams2(models.Model):
    
    coursenamefkey = models.ForeignKey(courseexam2, on_delete=models.DO_NOTHING,verbose_name="انتخاب آزمون")
    examquestion_published = models.BooleanField(default=True,verbose_name="نمایش یا عدم نمایش سوال")
    examquestion = RichTextField(verbose_name="متن سوال")
    examtext_published = models.BooleanField(default=False,verbose_name="نمایش یا عدم نمایش متن برای سوال")
    examtext = RichTextField(verbose_name="متن توضیحات برای سوال")
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




class examsanswer2(models.Model):
    coursenamefkey = models.ForeignKey(courseexam2, on_delete=models.DO_NOTHING,verbose_name="انتخاب آزمون")
    coursequestionfkey = ChainedForeignKey(
        exams2,
        related_name='coursequestionfkey',
        chained_field='coursenamefkey',
        chained_model_field='coursenamefkey',
        show_all=False,
        auto_choose=True,
        sort=True,
        help_text='سوال را انتخاب کنید',
    )
    examanswer_number = models.IntegerField(verbose_name="نمره جواب سوال")
    examanswer = models.TextField(max_length=50001, verbose_name="جواب سوال")
   
    def __str__(self):
        return self.examanswer
    class Meta:
        verbose_name_plural="ثبت جواب آزمون"




class UserAnswerTest(models.Model):
    
    courseexamfkey = models.TextField(verbose_name="آیدی درس")
    usernamefkey = models.TextField(verbose_name="آیدی کاربر")
    examquestionfkey = models.TextField(verbose_name="آیدی سوال")
    userexamanswer = models.TextField(verbose_name="جواب کاربر")
    
    def __str__(self):
        return self.userexamanswer
    class Meta:
        verbose_name_plural="جواب کاربر به سوال"
    











    
class exams(models.Model):
    examfileanswer = models.FileField(upload_to='courseexam/exams/%y/%m/%d/',blank=True)


