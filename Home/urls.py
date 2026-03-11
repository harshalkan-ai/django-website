from django.contrib import admin
from django.urls import path
from Home import views 

urlpatterns = [
    path("",views.index,name='Home'),
    path("services",views.services,name='services'),
    path("contact",views.contact,name='contact')
]