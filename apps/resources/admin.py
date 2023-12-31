from django.contrib import admin
from apps.resources import models
#from apps.resources.models import Departments

# Register your models here.
class AppointmentDetails(admin.ModelAdmin):
    list_display=('patient_name','doctor_name','date')
    
class ContactInfo(admin.ModelAdmin):
    list_display=('name','subject')
class RegistrationDetails(admin.ModelAdmin):
    list_display=('username','email','password')
    
class DeptDetail(admin.ModelAdmin):
    list_display=('dept_name','dept_image','description')
    
    
admin.site.register(models.Hospital)
admin.site.register(models.Appointments,AppointmentDetails)
admin.site.register(models.Contact,ContactInfo)
admin.site.register(models.Dept,DeptDetail)
admin.site.register(models.Registration,RegistrationDetails)

