from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(verbose_name='Name',max_length=50)

    email=models.EmailField()
    gender=models.CharField(verbose_name='Gender',max_length=50)
    city=models.CharField(verbose_name='City',max_length=50)
    dob=models.DateField()
    phone = models.CharField(verbose_name='Mobile Number', max_length=50)



def _str_(self):
    return self.name





