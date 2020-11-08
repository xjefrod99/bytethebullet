from django import forms
from .models import Announcement, Person

class AnnouncementForm(forms.ModelForm):

    class Meta:
        model = Announcement
        fields = ('text',)

class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ('name', 'contacts')
