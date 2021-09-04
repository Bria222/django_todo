from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import *
from .forms import *


def index(request):
    result= Task.objects.all()
    form = TaskForm

    if request.method == 'POST':
         form = TaskForm(request.POST)
         if form.is_valid:
            form.save()
         return redirect('/')

    context = {'result':result, 'form':form}
    return render(request, 'task/index.html',context)

def home(request):
    context = {}
    return render(request, 'task/home.html',context)

def update_task(request,pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid:
                form.save()
        return redirect('/')
    context = {'form':form}

    return render(request, 'task/update_task.html', context)

def deleteTask(request,pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
            item.delete()
            return redirect('/') 
    context = {'item':item}

    return render(request,'task/delete.html',context)


