from django.shortcuts import render, HttpResponse, redirect
from home.models import Task

def home(request):
    context = {'success': False}
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        print(title,desc)
        ins = Task(taskTitle=title, taskDesc=desc)
        ins.save()
        context = {'success': True}
        
    return render(request, 'index.html', context)

def tasks(request):
    allTasks = Task.objects.all()
    context = {'tasks': allTasks}
    return render(request, 'tasks.html', context)

def delete(request, task_id):
    dele = Task.objects.get(pk=task_id)
    dele.delete()
    return redirect('tasks.html')