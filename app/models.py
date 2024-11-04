from django.db import models

# Create your models here.
class services(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=600)
    image = models.ImageField(upload_to='mediaServices')

class galery(models.Model):
    service = models.ForeignKey(services,on_delete=models.CASCADE)
    imgs = models.ImageField(upload_to='mediaGalery')