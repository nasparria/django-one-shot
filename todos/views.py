# from django.shortcuts import render
from todos.models import TodoList

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.


class TodoListView(ListView):
    model = TodoList
    template_name = "todos/list.html"
    context_object_name = "todo_list"
    paginate_by = 3


class TodoListDetailView(DetailView):
    model = TodoList
    template_name = "todos/detail.html"
    context_object_name = "todo_list_detail"
