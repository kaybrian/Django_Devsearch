from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def Index(request):
    projects = Project.objects.all()
    print(projects)
    context = {'projects': projects}
    return render(request, 'projects.html', context)


def project(request, pk):
    project = Project.objects.get(id=pk)
    context = {'project': project}
    return render(request, 'single-project.html', context)
