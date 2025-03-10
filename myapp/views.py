#from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404 #Esta función nos permite devolver un objeto y si no, devuelve un error 404
from django.shortcuts import render, redirect
from .forms import CreateNewTask, CreateNewProject

# Create your views here.
def index(request):
    title = 'Django Course!!'
    return render(request, 'index.html', {'title':title})

def hello(request, username):
    print(username)
    return HttpResponse("<h2>Hello %s</h2>" % username) #Nos devolverá hello y el username que indiquemos en el buscador

def about(request):
    username = 'Christian'
    return render(request, 'about.html', {'username': username})

def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {'projects': projects})

def tasks(request):
    #get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html',{'form': CreateNewTask()})
    else:
        Task.objects.create(title=request.POST['title'],
        description=request.POST['description'], project_id=2)
        return redirect('tasks')
    
def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {'form': CreateNewProject()})
    else:       
        project = Project.objects.create(name=request.POST["name"])
        redirect('projects')

def project_detail(request, id):
    #project = Project.objects.get(id=id)
    project = get_object_or_404(Project, id=id) #Si no encuentra el proyecto, enviará un error 404
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html', {
        'project': project,
        'tasks': tasks
    })