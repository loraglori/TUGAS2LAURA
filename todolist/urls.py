from django.urls import path
from todolist.views import *

from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import create_task
from todolist.views import delete
from todolist.views import change

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create_task/', create_task, name='create_task'),
    path('delete/<int:id>', delete, name='delete'),
    path('change/<int:id>', change, name='change'),
    path('json/', show_todolist_json, name='show_todolist_json'),
    path('add/', add_task, name='add_task')
]