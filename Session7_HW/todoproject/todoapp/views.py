from django.shortcuts import render
from .models import Task
from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    tasks = Task.objects.order_by('duedate')

    return render(request, 'home.html', {'tasks': tasks})


def new(request):
    if request.method == 'POST':
        new_task = Task.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            duedate=request.POST['duedate']
        )
        return redirect('detail', new_task.pk)

    return render(request, 'new.html')


def detail(request, task_pk):
    task = Task.objects.get(pk=task_pk)

    return render(request, 'detail.html', {'task': task})


def edit(request, task_pk):
    task = Task.objects.get(pk=task_pk)

    if request.method == 'POST':
        Task.objects.filter(pk=task_pk).update(
            title=request.POST['title'],
            content=request.POST['content'],
            duedate=request.POST['duedate']
        )
        return redirect('detail', task_pk)

    return render(request, 'edit.html', {'task': task})


def delete(request, task_pk):
    task = Task.objects.get(pk=task_pk)
    task.delete()

    return redirect('home')
