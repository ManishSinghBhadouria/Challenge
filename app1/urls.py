from django.urls import path,include
from django.conf import settings
from . import views




urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('update1', views.update1, name='update1'),
    path('register', views.register, name='register'),
    path('iploc',views.iploc,name='iploc'),
    path('iploc1',views.iploc1,name='iploc1'),
    path('weather_data',views.weather_data,name='weather_data'),
    path('weather_data1',views.weather_data1,name='weather_data1'),
    ]