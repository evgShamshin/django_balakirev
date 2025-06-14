from audioop import reverse

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from website_app.models import About, Group, Tag
from website_users.forms import LoginUserForm


def login_user(request):
    data = {'title': 'ARO Group',
            'descr': """Плагин Connector - расширение для архитекторов и дизайнеров,
                                добавляющее возможности в Autodesk Revit.
                                Автоматизирует многие процессы и существенно сокращает время
                                создания модели.
                                Плагин совместим с 2019, 2020, 2021, 2022, 2023, 2024, 2025
                                версиями Autodesk Revit.""", }

    if request.method == 'POST':
        data['form'] = LoginUserForm(request.POST)
        if data['form'].is_valid():
            cd = data['form'].cleaned_data
            user = authenticate(request, username=cd['username'],
                                password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponse()
    else:
        data['form'] = LoginUserForm()

    return render(request, 'users/login.html', data)


def logout_user(request):
    logout(request)
    return HttpResponse()
