import json
from django.shortcuts import render, redirect
from .models import Todo, CompletedTodo
# from django.http.response import HttpResponse


def index(request):
    todos = Todo.objects.all()
    completed_todos = CompletedTodo.objects.all()
    context = {'todos': todos, 'completed_todos': completed_todos}
    return render(request, 'index.html', context)


def addNewTodo(request):
    if request.method == 'POST':
        todo = request.POST['todo']
        if not todo == '':
            newTodo = Todo.objects.create(task=todo)
        return redirect('/')

    return redirect('/')


def deleteTodo(request, id):
    if request.method == 'POST':
        todo = Todo.objects.get(id=id)
        todo.delete()

        return redirect('/')
    return redirect('/')


def completedTodo(request, id):
    if request.method == 'POST':
        todo = Todo.objects.get(id=id)
        completed_todo = CompletedTodo.objects.create(task=todo.task)
        todo.delete()
        return redirect('/')
    return redirect('/')


def deleteCompletedTodo(request, id):
    if request.method == 'POST':
        todo = CompletedTodo.objects.get(id=id)
        todo.delete()

        return redirect('/')
    return redirect('/')


def revertCompletedTodo(request, id):
    if request.method == 'POST':
        todo = CompletedTodo.objects.get(id=id)
        Todo.objects.create(task=todo.task)
        todo.delete()
        return redirect('/')
    return redirect('/')