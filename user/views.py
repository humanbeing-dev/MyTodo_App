from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from todo.models import Todo


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
    done = [task['project'] for task in Todo.objects.all().values() if task['complete']]
    undone = [task['project'] for task in Todo.objects.all().values() if not task['complete']]

    projects = []
    for name in names:
        projects.append({'names': name, 'done': done.count(name), 'undone': undone.count(name)})

    return render(request, 'user/profile.html', context={'projects': projects})
