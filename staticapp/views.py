from django.shortcuts import render
from .models import football,team

# Create your views here.


def index(request):
    obj=football.objects.all()
    teams = team.objects.all()
    return render(request, "index.html",{'result':obj,'team':teams})




# Create your views here.
