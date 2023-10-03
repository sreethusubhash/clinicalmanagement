from django.urls import path
from. import views

urlpatterns = [
    path('', views.login_resource),
    path('indexnew', views.indexnew),
    #path('index', views.index),
    path('register', views.register),
    
    
    path('text', views.text_utils),
    path('analyze', views.analyze),
    path('login',views.login),
    
    path('contact', views.contact),
    path('deptdetails',views.deptdetails),
    path('depturl', views.depturl),
    path('depturl2',views.depturl2),
    path('home', views.home),
]