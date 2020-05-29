from django.db import models

class linksAdmin(models.Model):
    
    title_page = models.CharField(max_length=500)
    pic = models.ImageField(upload_to='links/photos/%y/%m/%d/')
    title_links = models.CharField(max_length=500)
    
    
    def __str__(self):
        return self.title_page


class allLinks(models.Model):
    link_title = models.CharField(max_length=3000)
    link_url = models.CharField(max_length=3000)
    
    def __str__(self):
        return self.link_title