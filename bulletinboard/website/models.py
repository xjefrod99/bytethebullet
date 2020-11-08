from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    pass


class Person(models.Model):
    name = models.CharField(max_length = 30)
    contacts = models.ManyToManyField("self", blank = True, related_name="friends" )

    def __str__(self):
        return f"{self.name}"

    def get_friends(self):
        friends = self.contacts.all()
        return friends

    def get_queryset(self):
        return Person.objects.all()


class Announcement(models.Model):
    text = models.CharField(max_length=32,default='')
