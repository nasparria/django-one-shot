# from django.shortcuts import render
from django.urls import reverse_lazy
from todos.models import TodoList

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

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


class TodoListCreateView(CreateView):
    model = TodoList
    template_name = "todos/create.html"
    fields = ["name"]

    def get_success_url(self):
        return reverse_lazy("todo_list_detail", kwargs={"pk":self.object.pk})
