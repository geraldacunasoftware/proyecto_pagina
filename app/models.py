from django.db import models

# Create your models here.
class services(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=600)
    image = models.ImageField(upload_to='mediaServices')
