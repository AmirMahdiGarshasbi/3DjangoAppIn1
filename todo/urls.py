from django.urls import path
from . import views

urlpatterns = [
   path("todo/", views.todoListView, name="todo-list"),
   path("todo/<int:pk>", views.todoDetailView, name="todo-detail"),
   path("todo/<int:pk>/complete", views.TodoCompleteView.as_view(), name="todo-complete"),
   path("todo/<int:pk>/delete", views.TodoDeleteView.as_view(), name="todo-delete"),
]