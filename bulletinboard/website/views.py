from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from .models import Announcement
from .forms import AnnouncementForm, PersonForm

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

    if request.method == "POST":
        person_form = PersonForm(request.POST)
        if person_form.is_valid():

            knownPerson = Person.objects.get(name = request.POST.get("name"))
            if Person.objects.filter(name = request.POST.get("name")).exists():
                knownPerson.delete()
                person = person_form.save()
                return render(request, "website/contact.html",{
                    'person_form': PersonForm(),
                })
            else:
                person = person_form.save()
                return render(request, "website/contact.html",{
                    'person_form': PersonForm(),
                })



    person_form = PersonForm()
    simon = Person.objects.get(name= "Simon")
    print("these are simon's friends: ")
    print(simon.get_friends())
    # jiaqi = Person.objects.get(name= "Jiaqi")
    # print("these are Jiaqi's friends: ")
    # print(jiaqi.get_friends())
    return render(request, "website/contact.html",{
        'person_form': person_form,

    })
