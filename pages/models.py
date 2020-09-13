from django.db import models
from datetime import datetime

# Create your models here.

class Contact(models.Model):

  name = models.CharField(max_length=100)
  email = models.EmailField(max_length=254)
  message = models.TextField()
  is_active = models.BooleanField(default=False)
  created_at = models.DateTimeField(default = datetime.now)


  class Meta:
     verbose_name = 'contact'
     verbose_name_plural = 'contacts'
  



  def __str__(self):
       return self.email



class About(models.Model):
    title=models.CharField(max_length=254)
    description =models.TextField()
    image =models.ImageField(upload_to="about/")


class meta:
    verbose_name = 'about'
    verbose_name_plural = 'abouts'


    def __str_(self):
        return self.title


    



  
   
