from django.shortcuts import render

from todolist.models import Task

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login

from django.contrib.auth import logout
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required

from todolist.forms import TaskForm

from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.core import serializers


@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todo_user = Task.objects.filter(user=request.user)
    context = {
        'list_task': data_todo_user,
        'username': request.user.username,
        'form': TaskForm()
    }
    return render(request, 'todolist.html', context)

@login_required(login_url='/todolist/login/')
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            user = request.user
            Task.objects.create(title=title, description = description, date=datetime.datetime.now(), user=request.user)
            messages.success(request, "Your task has already saved!")
            return redirect("todolist:show_todolist")

    form = TaskForm();
    context = {'form':form, "username":request.user.username}
    return render(request, "create_task.html", context)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)            
            return redirect("todolist:show_todolist")
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect("todolist:login")

@login_required(login_url='/todolist/login/')
def delete(request, pk):
    Task.objects.filter(id=pk).delete()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def change(request,pk):
    status = Task.objects.get(id=pk)
    status.is_finished = not(status.is_finished)
    status.save()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def add_task(request):
    if request.method=="POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            task = Task.objects.create(title=title, description=description, date=datetime.date.today(), user=request.user)
            data = {
                "pk":task.pk,
                "title":task.title,
                "description":task.title,
                "is_finished":task.date
            }
            return JsonResponse(todo)

    return HttpResponseBadRequest()

@login_required(login_url='/todolist/login/')
def show_todolist_json(request):
    list_task = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", list_task), content_type="application/json")