from django.db import models

# Create your models here.
class Contact(models.model):
    name = models.CharField(max_length = 30)
    contacts = models.ManyToManyField("self", null= True, blank = True)
    #name.contacts.all()
