from django.urls import path
from. import views

urlpatterns = [
    path('list/', views.user_list),
    path('login/', views.user_login,name='login'),
    path('exercise/', views.exercise),
    
]