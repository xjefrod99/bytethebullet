from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

# Create your views here.
def index(request):
    return render(request, "website/index.html")

def contact(request):
    jeff = Person.objects.get(name= "Jeff")
    print(jeff.get_friends())
    alex = Person.objects.get(name= "Alex")
    print(alex.get_friends())
    return render(request, "website/contact.html")
