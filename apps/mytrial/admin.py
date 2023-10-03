from django.contrib import admin
from .models import Departments,Doctors,Booking

# apps.mytrial import models
# Register your models here.
class DoctorDetails(admin.ModelAdmin):
    list_display=('doc_name','doc_image')
class BookingAdmin(admin.ModelAdmin):
    list_display=('id','p_name','p_email','booking_date','booked_on')
admin.site.register(Departments)
admin.site.register(Doctors,DoctorDetails)
admin.site.register(Booking,BookingAdmin)

