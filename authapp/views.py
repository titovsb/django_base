from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
from django.urls import reverse
from authapp.forms import DebiUserLoginFrom, DebiUserCreationForm, DebiUserChangeForm
from authapp.models import DebiUser


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
    print('Метод', request.method)
    print('Метод', request.user)

    context = {
    'page_title': 'регистрация',
    'buttontext': 'зарегистрироваться',
    }


    if request.method == 'POST':
        form = DebiUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()         # магия - формируем модель
            if send_verify_mail(user):
                print('Сообщение о верификации отправлено')
                return HttpResponseRedirect(reverse('auth:login')) # после регистрации переадресация
            else:
                print('Ошибка отправки сообщения о верификации')
                return HttpResponseRedirect(reverse('auth:login')) # после регистрации переадресация
        else:
            print('форма не прошла валидацию')
            context['message'] = f'пользователь {request.POST.get("email")} уже существует'
    form = DebiUserCreationForm()
    context['form'] = form
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

def userlist(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('primary:index'))   # уходим на главную если мы не админ
    users = DebiUser.objects.all()
    context={
        'page_title': 'список пользователей',
        'users': users,
        }
    return render(request, 'authapp/userlist.html', context=context)

def send_verify_mail(user):
    verify_link = reverse('auth:verify', args=[user.email, user.activation_key])
    subject = f'Подтвердите регистрацию {user.username}'
    message = f'Для подтверждения регистрации перейдите по ссылке'\
    f'\n{settings.DOMAIN_NAME}{verify_link}'
    return send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email],
                     fail_silently=False)

def verify(request, email, activation_key):
    print(f'email: {email}, key: {activation_key}')
    try:
        user = DebiUser.objects.get(email=email)
        print(f'user: {user}')
        if user.activation_key == activation_key and not user.is_activation_expired():
            user.is_active = True
            user.save()
            auth.login(request, user)
            context={
                'page_title': 'проверка регистрации',
                'message': f'пользователь {user.username} зарегистрирован'
                }
            return render(request, 'authapp/verification.html', context=context)
            # return HttpResponseRedirect(reverse('primary:index'))
        else:
            context={
                'page_title': 'проверка регистрации',
                'message': f'ошибка регистрации пользователя {user.username}'
                }
            return render(request, 'authapp/verification.html', context=context)
    except Exception as e:
        print('Ошибка модуля регистрации')
        context={
            'page_title': 'проверка регистрации',
            'message': f'ошибка регистрации пользователя {email}'
            }
        return render(request, 'authapp/verification.html', context=context)
        # return HttpResponseRedirect(reverse('primary:index'))
