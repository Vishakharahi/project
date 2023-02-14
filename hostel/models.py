from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class HostelDetail(models.Model):
    image = models.ImageField(upload_to='images')  
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    studentcode = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    mobile=models.IntegerField(max_length=200)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname

   
    
class Contactus(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class studentdepartment(models.Model):
    Fullname = models.CharField(max_length=100)
    Field = models.CharField(max_length=100)
    Semester = models.CharField(max_length=100)
    Timming = models.CharField(max_length=100) 
    studentcode = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Fullname



class FoodMenu(models.Model):
    Days = models.CharField(max_length=100)
    Breakfast = models.CharField(max_length=100)
    Launch = models.CharField(max_length=100)
    Evening = models.CharField(max_length=100) 
    Dinner= models.CharField(max_length=100)
    AtNight= models.CharField(max_length=100)

    def __str__(self):
        return self.Days

class Feestructure(models.Model):
    Sno = models.CharField(max_length=100)
    Details = models.CharField(max_length=100)
    fee = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Sno
    
class studroom(models.Model):
    STUNAME = models.CharField(max_length=100)
    ROOMNO = models.CharField(max_length=100)
    BEDNO = models.CharField(max_length=100)
    MEMBERS = models.CharField(max_length=100)
    TABLE = models.CharField(max_length=100)
    CHAIR = models.CharField(max_length=100)
    CUPBOARD = models.CharField(max_length=100)
    
    def __str__(self):
        return self.STUNAME
    
    
class stuattendance(models.Model):
    STUNAME = models.CharField(max_length=100)
    DAYS = models.CharField(max_length=100)
    DATE = models.DateField(max_length=100)
    PRESENT = models.BooleanField(max_length=100)
    ABSENT = models.BooleanField(max_length=100)
    
    def __str__(self):
        return self.STUNAME
    
class stuentery(models.Model):
    STUNAME = models.CharField(max_length=100)
    DAYS = models.CharField(max_length=100)
    DATE = models.DateField(max_length=100)
    GOINGTIME = models.TimeField(max_length=100)
    COMINGTIME= models.TimeField(max_length=100)
    
    def __str__(self):
        return self.STUNAME


class feedback(models.Model):
    firstname = models.CharField(max_length=100)
    ln = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    
    def __str__(self):
        return self.firstname

class Booking(models.Model):
    Roomno = models.CharField(max_length=100)
    Price = models.CharField(max_length=100)
    MaxPerson = models.CharField(max_length=100)

    def __str__(self):
        return self.Roomno

class Bookingform(models.Model):
    Roomno = models.CharField(max_length=100)
    Fullname = models.CharField(max_length=100)
    Fathername = models.CharField(max_length=100)
    Mothername = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Fatheroccupation = models.CharField(max_length=100)
    Fathernumber = models.CharField(max_length=100)
    Studentnumber = models.CharField(max_length=100)

    def __str__(self):
        return self.Fullname

class Selectroom(models.Model):
    Roomno = models.CharField(max_length=100)

    def __str__(self):
        return self.Roomno




    

    
    