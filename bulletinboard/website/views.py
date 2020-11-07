from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from .models import Announcement
from .forms import AnnouncementForm

# Create your views here.

# def add_announcement(request):
#     if request.method == "POST":
#         form = AnnouncementForm(request.POST)
#         if form.is_valid():
#             announcement = form.save(commit=False)
#             announcement.save()
#         else:
#             return render(request, "tasks/add.html", {
#                 "form": form
#             })
#     else:
#         return render(request, "website/index.html", {
#             "announcements": Announcement.objects.all()
#         })


def index(request):
    return render(request, "website/index.html", {
        "anouncements": Announcement.objects.all()
    })

def contact(request):
    #simon = Person.objects.get(name= "Simon")
    #print(simon.get_friends())
    #jiaqi = Person.objects.get(name= "Jiaqi")
    #print(jiaqi.get_friends())
    return render(request, "website/contact.html")
