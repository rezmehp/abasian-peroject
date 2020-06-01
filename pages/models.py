from django.db import models

class footerAdmin(models.Model):
    title = models.CharField(max_length=2000)
    twitter = models.CharField(max_length=2000)
    twitter_published = models.BooleanField(default=True)
    linkedin = models.CharField(max_length=2000)
    linkedin_published = models.BooleanField(default=True)
    instagram = models.CharField(max_length=2000)
    instagram_published = models.BooleanField(default=True)
    mail = models.CharField(max_length=2000)
    mail_published = models.BooleanField(default=True)
    whatsapp = models.CharField(max_length=2000)
    whatsapp_published = models.BooleanField(default=True)
    telegram = models.CharField(max_length=2000)
    telegram_published = models.BooleanField(default=True)
    

    def __str__(self):
        return self.title



class sliderImage(models.Model):
    pic = models.ImageField(upload_to='slider/photos/%y/%m/%d/')




class ostanha(models.Model):
    ostanName = models.CharField(max_length=100)
    def __str__(self):
        return self.ostanName



class shahrha(models.Model):
    ostanNamefkey = models.ForeignKey(ostanha, on_delete=models.DO_NOTHING)
    shahrNames = models.CharField(max_length=100)
    def __str__(self):
        return self.shahrNames


        

class maghtaTahsili(models.Model):
    maghta = models.CharField(max_length=100)
    def __str__(self):
        return self.maghta



class reshteTahsili(models.Model):
    maghtafkey = models.ForeignKey(maghtaTahsili, on_delete=models.DO_NOTHING)
    reshte = models.CharField(max_length=100)
    def __str__(self):
        return self.reshte


class modaresin(models.Model):
    modares = models.CharField(max_length=300)
    email_modares = models.CharField(max_length=2000)
    def __str__(self):
        return self.modares