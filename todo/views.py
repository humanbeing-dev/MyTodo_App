from django.shortcuts import render, redirect
from .models import Todo, TodoArchive
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
    context = {'tasks': Todo.objects.all().order_by('-id')}
    return render(request, 'todo/home.html', context)


# class HomeView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'todo/chart.html')


@require_POST
def add_task(request):
    form = TodoForm(request.POST or None)

    task = request.POST['task']
    story = request.POST['story']
    project = request.POST['project']
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
            archive_todo = TodoArchive(task=todo.task, story=todo.story,
                                       project=todo.project, complete=todo.complete,
                                       date_added=todo.date_added)
            archive_todo.save()
            todo.delete()

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



