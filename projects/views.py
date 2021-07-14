from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required


def Index(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects.html', context)


def project(request, pk):
    project = Project.objects.get(id=pk)
    context = {'project': project}
    return render(request, 'single-project.html', context)


@login_required(login_url="login")
def Createproject(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'form-template.html', context)


@login_required(login_url="login")
def Updateproject(request, pk):
    profile = request.user.profile
    project = profile.profile_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'projects/projectform.html', context)


@login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.profile_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('index')
    context = {'object': project}
    return render(request, 'projects/deletetemplate.html', context)
