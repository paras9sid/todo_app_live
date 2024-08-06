from django.shortcuts import render
from todo_app.models import TaskToDo


def home(request):
    
    tasks_todo = TaskToDo.objects.filter(is_completed=False).order_by('-updated_at')
    # print(tasks_todo)   
    context = {
        'tasks_todo' : tasks_todo,
    }
    
    return render(request,'home.html',context)


def completed_tasks(request):
    completed_tasks = TaskToDo.objects.filter(is_completed=True)
    # print(completed_tasks)
    context = {
        'completed_tasks' : completed_tasks,
    }
    return render(request,'completed.html',context)
