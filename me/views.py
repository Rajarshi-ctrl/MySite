from django.shortcuts import render
from me.models import Contact
from django.contrib import messages
import datetime


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def skills(request):
    return render(request, 'skills.html')

def education(request):
    return render(request, 'education.html')

def project(request):
    return render(request, 'project.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        dt = str(datetime.datetime.now())

        contact = Contact(name=name, email=email, subject=subject, message=message, dt=dt)
        contact.save()

        messages.success(request, 'Thanks for your message. We will get in touch soon.')

    return render(request, 'contact.html')
