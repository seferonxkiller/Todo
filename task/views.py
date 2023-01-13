from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import EditForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


@login_required
def index(request):
    tasks = Task.objects.filter(user=request.user).order_by('-id').all()
    status = request.GET.get('f')
    if status:
        tasks = tasks.filter(status__contains=status)
    ctx = {
        'tasks': tasks
    }
    return render(request, 'task/index.html', ctx)


def edit(request, pk):
    obj = Task.objects.filter(id=pk).first()
    form = EditForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, f'<b>{obj.title}</b>')
        return redirect('/')
    ctx = {
        'obj': obj,
        'form': form
    }
    return render(request, 'task/edit.html', ctx)


@login_required
def create(request):
    form = EditForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect('/')
    ctx = {
        'form': form
    }
    return render(request, 'task/create.html', ctx)


@login_required
def delete(request, pk):
    obj = get_object_or_404(Task, id=pk)
    if request.user != obj.user:
        if not request.user.is_superuser:
            return HttpResponse("<h1>Rostan ham ochirmoqchimisz</h1>")
    ha = request.GET.get('ha')
    if ha:
        obj.delete()
        messages.error(request,  f"<b>{obj.title}</b> o'chirlidi")
        return redirect('/')
    ctx = {
        'object': obj
    }
    return render(request, 'task/delete.html', ctx)


def login_view(request):
    if not request.user.is_anonymous:
        return redirect('article:list')
    form = AuthenticationForm(request)
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_path = request.GET.get('next')
            messages.success(request, "Muvaffaqiyatli royhatdan otdingiz")
            if next_path:
                return redirect(next_path)
            return redirect('article:list')
    ctx = {
        'form': form
    }
    return render(request, 'task/login.html', ctx)


def logout_view(request):
    if not request.user.is_authenticated:
        return redirect('auth:login')
    if request.method == 'POST':
        messages.success(request, "Muvaffaqiyatli royxatdan chiqdingiz")
        logout(request)
        return redirect('auth:login')
    return render(request, 'task/logout.html')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('article:list')
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Muvaffaqiyatli royhatdan otdingiz")
        return redirect('auth:login')
    context = {
        'form': form
    }
    return render(request, 'task/register.html', context)