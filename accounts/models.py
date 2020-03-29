from django.db import models





class karbaruser1(models.Model):
    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    tell = models.IntegerField()
    melli_code = models.IntegerField()
    password = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    maghta = models.CharField(max_length=200)
    reshte = models.CharField(max_length=200)
    shahr = models.CharField(max_length=200)
    ostan = models.CharField(max_length=200)

    def __str__(self):
        return self.username
