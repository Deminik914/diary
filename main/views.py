from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SchoolForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group


def index(request):
    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                is_admin_diary = user.groups.filter(name='Administrator_dairy').exists()
                is_teacher = user.groups.filter(name='Teacher').exists()
                is_apprentice = user.groups.filter(name='Apprentice').exists()
                is_admin_school = user.groups.filter(name='Administrator_school').exists()
                if is_admin_diary:
                    return HttpResponse("<h1>Successful is_admin_diary </h1>")
                elif is_admin_school:
                    return HttpResponse("<h1>Successful is_admin_school </h1>")
                elif is_teacher:
                    return HttpResponse("<h1>Successful is_teacher </h1>")
                elif is_apprentice:
                    return HttpResponse("<h1>Successful is_apprentice </h1>")
        else:
            return render(request, 'main/error_auth.html')
    return render(request, 'main/index.html')


def administrator_panel(request):
    return render(request, 'main/administrator_panel.html')


def singup(request):
    form = SchoolForm()
    if request.method == 'POST':
        print(request.POST)
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form': form

    }

    return render(request, 'main/singup.html', context)
