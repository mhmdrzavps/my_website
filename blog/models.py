from django.db import models

# Create your models here.

class post(models.Model):
    title = models.CharField(length= 250)
    title = models.CharField(max_length = 255)
    content = models.TextField()
