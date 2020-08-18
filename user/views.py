from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from todo.models import Todo
from django.contrib.auth import get_user_model


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'user/register.html', context={'form': form})


@login_required
def profile(request):
    names = list({task['project'] for task in Todo.objects.all().values()})
    undone = [task['project'] for task in Todo.objects.all().values() if not task['complete']]
    done = [task['project'] for task in Todo.objects.all().values() if task['complete']]

    projects = []
    for name in names:
        projects.append({'names': name, 'done': done.count(name), 'undone': undone.count(name)})

    return render(request, 'user/profile.html', context={'projects': projects})


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        names = list({task['project'] for task in Todo.objects.all().values()})
        undone = [task['project'] for task in Todo.objects.all().values() if not task['complete']]
        done = [task['project'] for task in Todo.objects.all().values() if task['complete']]
        done_list = [done.count(name) for name in names]
        undone_list = [undone.count(name) for name in names]
        total_list = [done_list[i] + undone_list[i] for i in range(0, len(done_list))]

        labels = names
        data = {
            "labels": labels,
            "data1": done_list,
            "data2": undone_list,
            "total": total_list,
            }
        return Response(data)

