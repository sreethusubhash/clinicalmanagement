from django.db import models
from apps.core.models import CreatedModifiedDateTimeBase


# Create your models here.

class Hospital(CreatedModifiedDateTimeBase):
    hos_name=models.CharField(max_length=50)
class Appointments(CreatedModifiedDateTimeBase): 
    patient_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    telephone=models.CharField(max_length=50)
    date=models.DateField(auto_now_add=True)
    department=models.CharField(max_length=100)
    doctor_name=models.CharField(max_length=100)
    class Meta:
        verbose_name_plural='Appointments'
class Contact(CreatedModifiedDateTimeBase):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    subject=models.CharField(max_length=100)
    message=models.TextField(max_length=500)
    class Meta:
        verbose_name_plural='Contact'
class Dept(CreatedModifiedDateTimeBase):
    dept_name=models.CharField(max_length=100)
    description=models.TextField(max_length=500)
    dept_image=models.ImageField(upload_to='uploads')
    def __str__(self):
        return self.dept_name
class Registration(CreatedModifiedDateTimeBase):
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=20)
    phone_number=models.CharField(max_length=15)
    dateofbirth=models.DateField(max_length=10)
    class Meta:
        verbose_name_plural='Registration'

    
    
    
                             

 



    
    