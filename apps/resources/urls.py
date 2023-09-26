from django.urls import path
from. import views

urlpatterns = [
    path('', views.index),
     #path('', views.login),
     # path('index', views.index),
    
    
    path('text', views.text_utils),
    path('analyze', views.analyze),
    path('login',views.login),
    
    path('contact', views.contact),
    path('deptdetails',views.deptdetails),
    path('depturl', views.depturl),
    path('depturl2',views.depturl2),
    path('home', views.home),
]