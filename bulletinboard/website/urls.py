from django.urls import path, include,re_path
from . import views
from django.conf.urls import url

urlpatterns = [
    path("", views.index, name = "index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("contact", views.contact, name="contact"),
    path("add_announcement", views.add_announcement, name="add_announcement")
]
