import random
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.template.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm


def signinRender(request):
    return render(request, 'signin.html')


def signin(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        login = request.POST.get('login', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=login, password=password)
#        print(email, password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = 'Пользователь не найден'
            return render_to_response('signin.html', args)
    else:
        return render_to_response('signin.html', args)


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm
    if request.POST:
        newUser_form = UserCreationForm(request.POST)
        if newUser_form.is_valid():
            newUser_form.save()
            newUser = auth.authenticate(username=newUser_form.cleaned_data['username'], password=newUser_form.cleaned_data['password1'])
            auth.login(request, newUser)
            return redirect('/')
        else:
            args['form'] = newUser_form
    return render_to_response('register.html', args)


def signupRender(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        return signup(request)


def signup(request):
    login = request.POST['email']
    password = request.POST['password']
    rpassword = request.POST['rpassword']
    print(login, password, rpassword)
    return HttpResponseRedirect('/')


def index(request):
    number = random.randrange(0, 100)

    context = {
        'value': 'НАРУТО1',
        'number': str(number),
    }
    return render(request, 'index.html', context)

