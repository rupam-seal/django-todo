from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
    path("add/addmembers/", views.addmembers, name="addmembers"),
    path("delete/<int:id>", views.delete, name="delete"),
    path("update/<int:id>", views.update, name="update"),
    path("update/updatemember/<int:id>", views.updatemember, name="updatemember")
]