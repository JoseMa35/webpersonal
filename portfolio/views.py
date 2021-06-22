from django.shortcuts import render
from .models import Project, models

# Create your views here.
def portafolio(request):
    projects = Project.objects.all()
    return render(request,"portfolio/portfolio.html", {'projects':projects})
    #return render(request,"portfolio/portfolio.html")
