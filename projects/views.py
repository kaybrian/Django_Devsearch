from django.shortcuts import render, redirect
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

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'form-template.html', context)


def Updateproject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'projects/projectform.html', context)


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('index')
    context = {'object': project}
    return render(request, 'projects/deletetemplate.html', context)
