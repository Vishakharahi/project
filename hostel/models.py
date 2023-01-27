from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class HostelDetail(models.Model):
    image = models.ImageField(upload_to='images')  
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    studentcode = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    mobile=models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    Field = models.CharField(max_length=100)
    Semester = models.CharField(max_length=100)
    Timming = models.CharField(max_length=100) 
    
class Contactus(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    

    
    