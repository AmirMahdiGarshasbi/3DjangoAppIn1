from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from .models import Todo
from .forms import TodoForm

# Create your views here.
def todoListView(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo-list")

    todos = Todo.objects.all().order_by("-created_at")
    return render(request, 'todo/todo-list.html', {"todos": todos})

def todoDetailView(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    return render(request, 'todo/todo-detail.html', {"todo": todo})

class TodoCompleteView(UpdateView):
    model = Todo
    fields = ['title', 'context', 'status']

    def get_success_url(self):
        return reverse_lazy("todo-list")

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo-list')

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)