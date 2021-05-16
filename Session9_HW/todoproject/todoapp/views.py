from .models import Task, Comment
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    tasks = Task.objects.order_by('duedate')

    return render(request, 'home.html', {'tasks': tasks})


@login_required(login_url='/registration/login')
def mypage(request):
    mytask = Task.objects.filter(author=request.user).order_by('duedate')
    mycomment = Comment.objects.filter(author=request.user)
    return render(request, 'registration/mypage.html', {
        'mytask': mytask, 'mycomment': mycomment
    })


@login_required(login_url='/registration/login')
def new(request):
    if request.method == 'POST':
        new_task = Task.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            duedate=request.POST['duedate'],
            author=request.user
        )
        return redirect('detail', new_task.pk)

    return render(request, 'new.html')


def detail(request, task_pk):
    task = Task.objects.get(pk=task_pk)

    if request.method == "POST":
        content = request.POST['content']
        Comment.objects.create(
            task=task,
            content=content,
            author=request.user
        )
        return redirect('detail', task_pk)

    return render(request, 'detail.html', {'task': task})


def edit(request, task_pk):
    task = Task.objects.get(pk=task_pk)

    if request.method == 'POST':
        Task.objects.filter(pk=task_pk).update(
            title=request.POST['title'],
            content=request.POST['content'],
            duedate=request.POST['duedate']
        )
        return redirect('detail', task_pk)

    return render(request, 'edit.html', {'task': task})


def delete(request, task_pk):
    task = Task.objects.get(pk=task_pk)
    task.delete()

    return redirect('home')


def delete_comment(request, task_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('detail', task_pk)


def signup(request):
    if (request.method == 'POST'):
        found_user = User.objects.filter(username=request.POST['username'])
        if(len(found_user) > 0):
            error = '해당 USERNAME이 이미 존재합니다.'
            return render(request, 'registration/signup.html', {'error': error})
        new_user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
        auth.login(request, new_user)
        return redirect('home')

    return render(request, 'registration/signup.html')


def login(request):
    if (request.method == 'POST'):
        found_user = auth.authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if(found_user is None):
            error = '아이디 또는 비밀번호가 틀렸습니다.'
            return render(request, 'registration/login.html', {'error': error})
        auth.login(request, found_user)
        return redirect('home')

    return render(request, 'registration/login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')
