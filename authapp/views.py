from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from django.urls import reverse

from authapp.forms import DebiUserLoginFrom


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

