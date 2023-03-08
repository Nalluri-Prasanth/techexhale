from django.urls import path
from . import views

app_name = "mainpage"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("contact", views.contact, name="contact"),
]