from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    url = models.URLField(null=True,blank=True)
    descrip = models.CharField(max_length=200, blank=False, default='')
