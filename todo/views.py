from django.shortcuts import render

from todo.models import Todo


def todo_list(request):
    todos=Todo.objects.all()
    context={
        'todos': todos
    }
    return render(request, 'pages/todo_list.html', context)

  