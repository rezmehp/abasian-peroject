from django.db import models

class contactAdmin(models.Model):
    title_page = models.CharField(max_length=200)
    pic = models.ImageField(upload_to='contact/photos/%y/%m/%d/')
    title_message = models.CharField(max_length=200)
    click = models.CharField(max_length=30)
    address = models.TextField(blank=True)
    def __str__(self):
        return self.title_page