from re import X, template
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader

from members.models import Members

# Create your views here.
def index(request):
    template = loader.get_template("index.html")

    member = Members.objects.all().values()

    context = {
        'member' : member,
    }

    return HttpResponse(template.render(context, request))

def add(request):
    template = loader.get_template("add.html")
    return HttpResponse(template.render({}, request))

def addmembers(request):
    x = request.POST['name']
    y = request.POST['age']

    member = Members(fullname=x, age=y)
    member.save()

    return HttpResponseRedirect(reverse("index"))

def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()

    return HttpResponseRedirect(reverse("index"))

def update(request, id):
    template = loader.get_template("update.html")

    member = Members.objects.get(id=id)

    context = {
        'member' : member,
    }

    return HttpResponse(template.render(context, request))

def updatemember(request, id):
    x = request.POST["name"]
    y = request.POST["age"]

    member = Members.objects.get(id=id)
    member.fullname = x
    member.age = y

    member.save()

    return HttpResponseRedirect(reverse("index"))