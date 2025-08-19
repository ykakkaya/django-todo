from django.shortcuts import get_object_or_404, render

from todo.models import Todo


def todo_list(request):
    todos=Todo.objects.all()
    context={
        'todos': todos
    }
    return render(request, 'pages/todo_list.html', context)

def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    context = {
        'todo': todo
    }
    return render(request, 'pages/todo_detail.html', context)