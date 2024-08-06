from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import TaskToDo
from .forms import TaskToDoForm


def addTask(request):

    if request.method == 'POST':
        
        form = TaskToDoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print('form is invalid')
            print(form.errors)
        
    form = TaskToDoForm()
    
    context = {
        'form':form,
    }
    
    return render(request,'addTask.html',context)

def mark_as_done(request,pk):
    
    task = get_object_or_404(TaskToDo,pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')
    
    
def mark_as_undone(request,pk):
    
    task = get_object_or_404(TaskToDo, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def editTask(request,pk):
    
    task = get_object_or_404(TaskToDo, pk=pk)    
    if request.method == 'POST':
        form = TaskToDoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')     
        
    form = TaskToDoForm(instance=task)   
    context = {
        'form': form,
        'task': task,
    }
    return render(request,'editTask.html',context)
        
def deleteTask(request,pk):
    task = get_object_or_404(TaskToDo, pk=pk)   
    task.delete()
    return redirect('home')