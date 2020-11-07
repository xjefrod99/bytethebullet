from django.db import models

# Create your models here.
class Announcement(models.Model):
    text = models.CharField(max_length=32,default='')


class Person(models.Model):
    name = models.CharField(max_length=32,default='')
    contacts = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return f"{self.name}: {self.contacts}"
