from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Appointments,Contact,Dept,Registration
from apps.user.models import User


# Create your views here.
def register(request):
    if request.method =='POST':
        
        obj=Registration()
        obj.username=request.POST['uname']
        obj.email=request.POST['email']
        obj.password=request.POST['psw']
        obj.phone_number=request.POST['pn']
        obj.dateofbirth=request.POST['db']
        obj.save()
        return HttpResponseRedirect('register')
    return render(request,'resources1/registration.html')

def login_resource(request):
    if request.method == 'POST':
        username = request.POST["uname"]
        password = request.POST["psw"]
        try:
            var=Registration.objects.get(username=username,password=password)#model(username)=views(un)
            return HttpResponseRedirect('indexnew')
        #if var:
        except:
            msg =('Invalid username or password')
            return render(request,'resources1/loginresource.html',{'m':msg})
    return render(request,'resources1/loginresource.html')

def indexnew(request):
    return render(request,'resources1/index.html')

def login(request):
    #if request.method =='POST':
        # obj=login()
        # obj.Username=request.POST['uname']
        # obj.Password=request.POST['psw']
    return render(request,'resources1/login.html')

def depturl2(request):
    data=Dept.objects.all()
    #dept_data=Dept.objects.get(id=2)
    # q=request.GET['uid']
    # if q:
    #     var=Dept.objects.get(id=id)
    #     return render(request,'resources1/depturl2.html',{'dept_data':var})
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
def text_utils(request):
    return render(request,'resources1/textutils.html')
def analyze(request):
    if request.method =='GET':
        t=request.GET.get('textname')
        c=request.GET.get('removepunc','off')
        capitalized_text=request.GET.get('cap_txt')
        lowercase_text=request.GET.get('lower_txt')
        
        punctuations="!#$%&'()*+, -./:;<=>?@[\]^_`{|}~"
        analyzed=''
        if c=='on':
            
            for char in t:
                if char not in punctuations:
                    analyzed+=char
            
        # else:
        #     return HttpResponse('Error')
        
        if capitalized_text=='on':
            analyzed=t.upper()
            
        if lowercase_text=='on':
            analyzed=t.lower()
            
        data={'djtext':analyzed}
    return render(request,'resources1/analyze.html',data)
