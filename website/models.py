from django.db import models

# Create your models here.



class Contact(models.Model):

    name= models.CharField(max_length= 255)
    email= models.EmailField()
    subject= models.CharField(max_length= 255)
    message= models.TextField()
    created_date = models.DateTimeField(auto_now_add= True)
    updated_date = models.DateTimeField(auto_now= True)

    class Meta:
        ordering = ['name']
        #verbose_name = 'پست'
        #verbose_name_plural = 'پستها'

    def __str__(self):
        return '{} - {}'.format(self.name, self.id)

class Newsletter(models.Model):

    email = models.EmailField()

    def __str__(self):
        return str(self.email)

       