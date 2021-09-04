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
    context = {}
    return render(request, 'task/update_task.html', context)

