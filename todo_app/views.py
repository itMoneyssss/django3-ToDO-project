from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import ToDoForm
from .models import Todo


def home(request):
    return render(request, 'todo_app/home.html')


def home2(request):
    return render(request, 'todo_app/home2.html')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo_app/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currentToDos')
            except IntegrityError:
                return render(request, 'todo_app/signupuser.html',
                              {'form': UserCreationForm(), 'error': "That name has already been taken. Please choose "
                                                                    "a new username."})
        else:
            return render(request, 'todo_app/signupuser.html',
                          {'form': UserCreationForm(), 'error': "Passwords do not match. Please try again."})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todo_app/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'todo_app/loginuser.html',
                          {'form': AuthenticationForm(), 'error': 'Username or password error '})
        else:
            login(request, user)
            return redirect('currentToDos')


@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect("home")
    else:
        logout(request)
        return redirect("home")


@login_required
def createToDos(request):
    if request.method == 'GET':
        return render(request, 'todo_app/createToDos.html', {'form': ToDoForm()})
    else:
        try:
            form = ToDoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('currentToDos')
        except ValueError:
            return render(request, 'todo_app/createToDos.html', {'form': ToDoForm(), 'error': 'Bad request'})


@login_required
def currentToDos(request):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'todo_app/currentToDos.html', {'todos': todos})


@login_required
def completedToDos(request):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'todo_app/completedToDos.html', {'todos': todos})


@login_required
def viewToDos(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'GET':
        form = ToDoForm(instance=todo)
        return render(request, 'todo_app/viewToDos.html', {'todos': todo, 'form': form})
    else:
        try:
            form = ToDoForm(request.POST, instance=todo)
            form.save()
            return redirect('currentToDos')
        except ValueError:
            return render(request, 'todo_app/viewToDos.html', {'todos': todo, 'form': form, 'error': 'Bad info'})


@login_required
def completeToDos(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.datecompleted = timezone.now()
        todo.save()
        return redirect('currentToDos')


@login_required
def deleteToDos(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.datecompleted = timezone.now()
        todo.delete()
        return redirect('currentToDos')


@login_required
def instruction(request):
    return render(request, 'todo_app/instruction.html')


@login_required
def link(request):
    return render(request, 'todo_app/link to authors.html')


@login_required
def donate(request):
    return render(request, 'todo_app/support.html')


def error_404(request, exseption):
    return render(request, '404.html')


