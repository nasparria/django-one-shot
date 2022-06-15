from unicodedata import name
from django.urls import path

from todos.views import (
    TodoListView,
    TodoListDetailView,
    TodoListCreateView,
    TodoListUpdateView,
    TodoListDeleteView

)

urlpatterns = [
  path("", TodoListView.as_view(), name="todo_list"),
  path("<int:pk>/", TodoListDetailView.as_view(), name="todo_list_detail"),
  path("create/", TodoListCreateView.as_view(), name="todo_list_create"),
  path("<int:pk>/edit/", TodoListUpdateView.as_view(), name="todo_list_edit"),
  path("<int:pk>/delete/", TodoListDeleteView.as_view(), name="todo_list_delete"),

]
