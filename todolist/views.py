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

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todo_user = Task.objects.filter(user=request.user)
    context = {
        'list_task': data_todo_user,
    }
    return render(request, 'todolist.html', context)

@login_required(login_url='/todolist/login/')
def create_task(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        title = form.cleaned_data["title"]
        description = form.cleaned_data["description"]
        user = request.user
        task = Task(title=title, description = description, user=user)
        task.save()

        return redirect("todolist:show_todolist")


    context = {'form':form}
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
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

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