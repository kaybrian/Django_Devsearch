from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import ProjectForm, ReviewForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .utils import searchProject, paginationProjects
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages


def Index(request):
    projects, search_query = searchProject(request)
    custom_range, projects = paginationProjects(request, projects, 6)
    context = {'projects': projects,
               'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'projects.html', context)


def project(request, pk):
    project = Project.objects.get(id=pk)
    form = ReviewForm()
    if request.method == 'POST':
        if form.is_valid(request.POST):
            review = form.save(commit=False)
            review.project = project
            review.owner = request.user.profile
            review.save()

            # update project votecount
            messages.success(request, "Your Review has been Submitted")
    context = {'project': project, 'form': form}
    return render(request, 'single-project.html', context)


@ login_required(login_url="login")
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


@ login_required(login_url="login")
def Updateproject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'form-template.html', context)


@ login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('index')
    context = {'object': project}
    return render(request, 'deletetemplate.html', context)
