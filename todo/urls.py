from django.urls import path

from todo.views import todo_detail, todo_list

urlpatterns = [
    path('',todo_list, name='home'),
    path('todo/<int:pk>/', todo_detail, name='todo_detail'),
]