from django.contrib import admin
from .models import Person

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    pass


admin.site.register(Person, PersonAdmin)
