import email
from email import message
import numbers
from unicodedata import name
from django.db import models

# Create your models here.
#Create table
class Contact(models.Model):
    name = models.CharField(max_length=50,null=True)
    email = models.EmailField(max_length= 100,null=True)
    message = models.TextField(max_length=450,null=False)
    
    def __str__(self):
        return self.email