from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context ={ 
        "variable":"this is sent"
    }
    return render(request, 'index.html',context)
    
def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method=="POST":
        email=request.POST.get("email")
        name=request.POST.get("name")
        age=request.POST.get("age")
        password=request.POST.get("password")
        contact=Contact(email=email,name=name,age=age,password=password,date=datetime.today())
        contact.save()
        messages.success(request, "Your Message has been sent.")
    return render(request, 'contact.html')
