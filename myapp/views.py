from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewTask, CreateNewProject

# Create your views here.
def index(request):
    title = 'Django Course!!'
    return render(request, 'myapp/index.html', {'title':title})

def hello(request, name):
    print(name)
    return HttpResponse("<h1>Hello %s </h1>" %name)

def about(request):
    return render(request, 'myapp/about.html')

def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {'projects': projects})

def tasks(request):
    #task = get_object_or_404(Task, id=id)
    #task = Task.objects.get(title=title)
    tasks = Task.objects.all()

    return render(request, 'myapp/task.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect('tasks')

    return render(request, 'myapp/create_task.html', {'form': CreateNewTask()})

def create_project(request):
    if request.method == 'POST':
        name = request.POST['name']
        if name:
            Project.objects.create(name=name)
            return redirect('projects')
    
    return render(request, 'projects/create_project.html', {'form': CreateNewProject()})

def project_detail(request, id):
    print(id)
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html', {
        'project': project,
        'tasks': tasks
    })