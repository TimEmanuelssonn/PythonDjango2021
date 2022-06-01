from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'projects/singel-project.html', {'project':projectObj})

def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        #With request.FILES we can get our image files the user upload
        form = ProjectForm(request.POST, request.FILES)
        #if everything is valid and correct
        if form.is_valid():
            #save from to database
            form.save()
            #redirect to projects side
            return redirect('projects')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)


def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    #project from will fill in id/pk data in the form
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        #if everything is valid and correct
        if form.is_valid():
            #save from to database
            form.save()
            #redirect to projects side
            return redirect('projects')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)

def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
        
    context = {'object':project}
    return render(request, 'projects/delete_template.html', context)