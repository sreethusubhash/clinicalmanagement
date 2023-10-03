from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments,Doctors
from .forms import BookingForm

# Create your views here.
def home(request):
    # person={
    #     'name':'sreethu',
    #     'place':'Berlin'
    # }
    # person={
    #     'num1':0
    # }
    person={'num':[1,2,3,4,5]}
    return render(request,'mytrial1/index.html',person)
def about(request):
    
    return render(request,'mytrial1/about.html')
def booking(request):
    
    if request.method == 'POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'mytrial1/booking_confirmation.html')
        
    form=BookingForm()
    dict_form={'form':form}
    return render(request,'mytrial1/booking.html',dict_form)

def contact(request):
    return render(request,'mytrial1/contact.html')
def doctor(request):
    dict_docs={'doctors':Doctors.objects.all()}
    return render(request,'mytrial1/doctor.html',dict_docs)
def department(request):
    dict_dept={
        'dept':Departments.objects.all()
    }
    return render(request,'mytrial1/department.html',dict_dept)
