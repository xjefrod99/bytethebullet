from django.urls import path, include,re_path
from . import views
from django.conf.urls import url

urlpatterns = [
path("", views.index, name = "index"),
]
