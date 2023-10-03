from django.urls import path
from. import views


urlpatterns = [
    path('index', views.home,name='home'),
    path('contact', views.contact,name='contact'),
    path('booking', views.booking,name='booking'),
    path('about', views.about,name='about'),
    path('doctor', views.doctor,name='doctor'),
    path('department', views.department,name='department'),
]