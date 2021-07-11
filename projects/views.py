from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import ProjectForm


def Index(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects.html', context)


def project(request, pk):
    project = Project.objects.get(id=pk)
    context = {'project': project}
    return render(request, 'single-project.html', context)


def Createproject(request):
    form = ProjectForm()
    context = {'form': form}
    return render(request, 'projectform.html', context)
