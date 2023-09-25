from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Appointments,Contact,Dept



# Create your views here.
def depturl2(request):
    data=Dept.objects.all()
    #dept_data=Dept.objects.get(id=2)
    return render(request,'resources1/depturl2.html',{'data':data})

def depturl(request):
    qstring=request.GET['uid']
    dept_data=Dept.objects.get(id=qstring)
    return render(request,'resources1/depturl.html',{'dept_data':dept_data})

    
def deptdetails(request):
    data=Dept.objects.all()
    #dept_data=Dept.objects.get(id=2)#return render(request,'resources1/index.html',{'data':data,'dept_data':dept_data})
    return render(request,'resources1/index.html',{'data':data})
    
    
def home(request):
    data=Dept.objects.all()
    context={'data':data}
    return render(request,'resources1/home.html',context)
                  
def index(request):
    
    if request.method =='POST':
        
        obj=Appointments()
        obj.patient_name=request.POST['patient_name']
        obj.email=request.POST['email']
        obj.telephone=request.POST['phone']
        obj.date=request.POST['date']
        obj.department=request.POST['department']
        obj.doctor_name=request.POST['doctor']
        obj.save()
        return HttpResponseRedirect('/')
    return render(request,'resources1/index.html')
def contact(request):
    if request.method =='POST':
        
        obj=Contact()
        obj.name=request.POST['name']
        obj.email=request.POST['email']
        obj.subject=request.POST['subject']
        obj.message=request.POST['message']
       
        obj.save()
        return HttpResponseRedirect('/')
    return render(request,'resources1/contact.html')
