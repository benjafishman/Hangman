from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
#from home.forms import UserForm, User
from home.forms import UserCreateForm
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
            #authenticate user then login
            user = authenticate(username=username, password=password)

            login(request, user)

            return HttpResponseRedirect(reverse('minyan_mailer:index'))
    else:
        form = UserCreateForm()
    return render(request, "registration/register.html", {
        'form': form,
    })