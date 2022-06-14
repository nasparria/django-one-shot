# from django.shortcuts import render
from todos.models import TodoList

from django.views.generic.list import ListView

# Create your views here.


class TodoListView(ListView):
    model = TodoList
    template_name = "todos/list.html"
    context_object_name = "todolists"
    paginate_by = 3
