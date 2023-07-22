from django.db import models

# Create your models here.
class Photo(models.Model):
    photo   = models.ImageField(null=True,blank=True,upload_to='images/')
    created = models.DateTimeField(auto_now_add=True, null=True)
    