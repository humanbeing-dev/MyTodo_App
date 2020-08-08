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
    projects = list({task['project'] for task in Todo.objects.all().values()})
    print(projects)
    return render(request, 'user/profile.html', context={'projects': projects})
