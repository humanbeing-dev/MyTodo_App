from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Todo
from django.utils import timezone
from django.views.decorators.http import require_POST
from .forms import TodoForm
from django.contrib import messages
from django.http import JsonResponse
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model



def home(request):
    context = {'tasks': Todo.objects.filter(archived=False).order_by('-id')}
    return render(request, 'todo/home.html', context)


@require_POST
def add_task(request):
    form = TodoForm(request.POST or None)

    task = request.POST['new_task']
    story = request.POST['new_story']
    project = request.POST['new_project']
    Todo.objects.create(task=task, story=story, project=project)

    return redirect('home')


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


def archive_completed(request):
    for todo in Todo.objects.all():
        if todo.complete:
            todo.archived = True
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
    context = {'task': todo.task, 'story': todo.story, 'project': todo.project, 'id': todo.id}
    return render(request, 'todo/edit.html', context)


def save(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.task = request.POST['task']
    todo.story = request.POST['story']
    todo.project = request.POST['project']
    todo.save()

    return redirect('home')


def project(request, todo_id):
    """View with projects and its list of done and undone tasks"""
    current_project = Todo.objects.get(pk=todo_id).project
    undone = Todo.objects.filter(Q(project=current_project) & Q(complete=False))
    done = Todo.objects.filter(Q(project=current_project) & Q(complete=True))
    context = {'done': done, 'todos': undone}

    return render(request, 'todo/projects.html', context)
