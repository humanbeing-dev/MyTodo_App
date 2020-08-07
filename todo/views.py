from django.shortcuts import render, redirect
from .models import Todo
from django.utils import timezone
from django.views.decorators.http import require_POST
from .forms import TodoForm
from django.contrib import messages


def home(request):
    context = {'tasks': Todo.objects.all().order_by('-id')}
    return render(request, 'todo/home.html', context)


@require_POST
def add_task(request):
    form = TodoForm(request.POST or None)

    task = request.POST['task']
    project = request.POST['project']
    Todo.objects.create(task=task, project=project)

    return redirect('home')

# def add_task(request):
#     if request.method == "POST":
#         form = TodoForm(request.POST or None)
#
#         if form.is_valid():
#             form.save()
#             messages.success(request, ('Item has been added to list!'))
#             return redirect('home')
#
#     else:
#         context = {'tasks': Todo.objects.all().order_by('-id')}
#         return render(request, 'todo/home.html', context)


#



def completed_task(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('home')


def uncompleted_task(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = False
    todo.save()

    return redirect('home')


def delete_completed(request):
    Todo.objects.filter(complete=True).delete()

    return redirect('home')


def delete_all(request):
    Todo.objects.all().delete()

    return redirect('home')


def delete_one(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.delete()

    return redirect('home')


def edit(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    context = {'task': todo.task, 'project': todo.project, 'id': todo.id}
    return render(request, 'todo/edit.html', context)


def save(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.task = request.POST['task']
    todo.project = request.POST['project']
    todo.save()

    return redirect('home')
