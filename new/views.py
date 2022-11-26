from cgitb import html
import email
from email import message
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact


# Create your views here.

def home(request):
    return render(request,'home.html')
def work(request):
    return render(request,'work.html')
def self(request):
    return render(request,'self.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        #objectCreate
        contacts = Contact()
        contacts.name = name
        contacts.email = email
        contacts.message = message
        contacts.save()
        return HttpResponse('<h1> Thanks for Contact with us! </h1>')

    return render(request,'contact.html')

def showdata(request):
    contacts = Contact.objects.all()
    for i in contacts:
      print(i.id,i.name,i.email,i.message)
    data = {'contact':contacts}
    return render(request,'showdata.html',data)