from django.db import models
from django.contrib.auth.models import User
from accounts.models import karbaruser1
from datetime import datetime

class contactAdmin(models.Model):
    title_page = models.CharField(max_length=200)
    pic = models.ImageField(upload_to='contact/photos/%y/%m/%d/')
    title_message = models.CharField(max_length=200)
    click = models.CharField(max_length=30)
    address = models.TextField(blank=True)
    def __str__(self):
        return self.title_page


class contactuserpayam4(models.Model):
    usernamefkey = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    soal = models.TextField(blank=True)
    javabadmin = models.TextField(blank=True)
       
    def __str__(self):
        return self.usernamefkey 



class contactuserpm(models.Model):
    usernamefkey = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    soal = models.TextField(blank=True)
    javabadmin = models.TextField(blank=True)
  
    def __str__(self):
        return str(self.usernamefkey) if self.usernamefkey else ''