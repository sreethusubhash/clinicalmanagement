from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import User
from django.contrib.auth import authenticate,login
#from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def exercise(request):
    return render(request,'user/exercise.html')

def user_list(request):
    users=User.objects.all()
    context={'users':users}
    return render(request,'user/user_list.html',context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get("uname")
        password = request.POST.get("psw")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # The intended view to redirect to after a successful login.
            return redirect('login')#view name
            #return render(request,'resources1/index.html')
        else:
            
            return render(request, 'user/login.html', {'error_message': 'Invalid credentials'})
# def login(request):
    return render(request,'user/login.html')

# def user_login(request):
#     error_message="None"
#     form=AuthenticationForm(data=request.POST)
#     if request.method == 'POST':
#         form=AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             username=form.cleaned_data.get('uname')
#             password=form.cleaned_data.get('psw')
#             user=authenticate(
#                 username=username,
#                 password=password,
#             )
#             if user is not None:
#                 #use the session to keep the authenticated user's id
#                 login(request,use# Authentication failed, handle accordingly (e.g., display an error message)r)
#                 redirect('login')
                
#         else:
#             #user's data is not valid,set an error msg to be displayed
#             error_message='Sorry,something went wrong.Try again..'
#     context={'form':form,'error_message':error_message}
#     return render(request,'user/login.html',context)
