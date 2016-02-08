from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.contrib.auth import authenticate, login as auth_login

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
# from home.forms import UserForm, User
from home.forms import UserCreateForm, AuthenticateForm
# Create your views here.

def index(request):
    return render(request, 'home/index.html')


def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()

            username = request.POST['username']
            password = request.POST['password1']
            # authenticate user then login

            user = authenticate(username=username, password=password)

            auth_login(request, user)
            return HttpResponseRedirect(reverse('motivator:index'))
    else:
        form = UserCreateForm()
    return render(request, "registration/register.html", {
        'form': form,
    })


def login(request):
    '''
print("hello world 1")
form = AuthenticateForm()
if request.method == 'POST':
    print(form.is_valid())
    if form.is_valid():
        print("hello world 2")
        form = AuthenticateForm(data=request.POST)
        # if form.is_valid():
        print("hello world 3")
        username = request.POST['username']
        password = request.POST['password']
        print("here 0")
        user = authenticate(username=username, password=password)
        print("here 2")
        if user is not None:
            print("here 2")
            if user.is_active:
                auth_login(request, user)
                # Redirect to a success page.
                return HttpResponseRedirect(reverse('minyan_mailer:index'))
            else:
                # Return a 'disabled account' error message
                print('account disabled')
    else:
        # Return an 'invalid login' error message.
        print('invalid login, try again')
        form = AuthenticateForm(data=request.POST)

print(form.errors)


return render(request, "registration/login.html", {
    'form': form,
})
'''
    form = AuthenticateForm(data=request.POST or None)
    print("hello world")
    if request.POST and form.is_valid():
        print("here")
        user = form.login(request)
        if user:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('minyan_mailer:index'))  # Redirect to a success page.
    errors = form.errors
    return render(request, "registration/login-v2.html", {'form': form, 'errors':errors})

