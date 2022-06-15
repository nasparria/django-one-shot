from django.urls import path

from todos.views import (
    TodoListView,
    TodoListDetailView,
    TodoListCreateView,

)

urlpatterns = [
  path("", TodoListView.as_view(), name="todo_list"),
  path("<int:pk>/", TodoListDetailView.as_view(), name="todo_list_detail"),
  path("create/", TodoListCreateView.as_view(), name="todo_list_create")

]
