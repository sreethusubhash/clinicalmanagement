from django.urls import path
from. import views

urlpatterns = [
    path('', views.index),
    path('contact', views.contact),
   
    path('deptdetails',views.deptdetails),
    path('depturl', views.depturl),
    path('depturl2',views.depturl2),
    path('home', views.home),
]