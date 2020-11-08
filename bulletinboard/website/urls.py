from django.urls import path, include,re_path
from . import views
from django.conf.urls import url

urlpatterns = [
    path("index", views.index, name = "index"),
    path("", views.contact, name="contact")
]
