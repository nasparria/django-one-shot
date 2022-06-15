from django.urls import path

from todos.views import (
    TodoListView,
    TodoListDetailView,
)

urlpatterns = [
  path("", TodoListView.as_view(), name="todo_list"),
  path("<int:pk>/", TodoListDetailView.as_view(), name="todo_list_detail"),

]
