from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting, Room


def welcome(request):
    return render(request, "website/welcome.html",
                  {"message": "This data was sent from the view",
                   "x": 42,
                   "meetings": Meeting.objects.all(),
                   "rooms": Room.objects.all()})


def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))


def about(request):
    return HttpResponse("Hi my name is Erdogan I'm a new python Django developer")
