from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from django.urls import reverse

from authapp.forms import DebiUserLoginFrom, DebiUserCreationForm, DebiUserChangeForm


def login(request):
    if request.method == 'POST':
        form = DebiUserLoginFrom(data=request.POST)
        if form.is_valid():
            username= request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            print(user)
            if user and user.is_active:
                auth.login(request, user)   # cookie created
                return HttpResponseRedirect(reverse('primary:index'))
                # return HttpResponseRedirect('/')
    else:
        form = DebiUserLoginFrom()

    title = 'Логинимся'
    context = {'page_title':title,
               'form': form}
    return render(request, 'authapp/login.html', context=context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('primary:index'))

def registration(request):
    if request.method == 'POST':
        form = DebiUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()         # магия - формируем модель
            return HttpResponseRedirect(reverse('auth:login')) # после регистрации переадресация
    else:
        form = DebiUserCreationForm()

    context = {
        'page_title': 'регистрация',
        'form': form,
        'buttontext':'зарегистрироваться',
        }
    return render(request, 'authapp/regupdate.html', context=context)

def edit(request):
    if request.method == 'POST':
        form = DebiUserChangeForm(request.POST, request.FILES,
                                  instance=request.user)
        if form.is_valid():
            form.save()         # магия - формируем модель
            # return HttpResponseRedirect(reverse('auth:edit')) # после регистрации переадресация
            return HttpResponseRedirect(request.path_info) # пойти откуда пришли
    else:
        form = DebiUserChangeForm(instance=request.user)

    context = {
        'page_title': 'изменение',
        'form': form,
        'buttontext':'сохранить изменения',
        }
    return render(request, 'authapp/regupdate.html', context=context)
