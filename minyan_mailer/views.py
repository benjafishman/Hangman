from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from minyan_mailer.models import Minyan, Davening, DaveningForm
from minyan_mailer.forms import MinyanForm, UserForm, User
# Create your views here.


def index(request):
    print(request)
    if not request.user.is_authenticated():
        print('not authenticated')
    if request.method == 'GET':
        form = MinyanForm()
    else:
        form = MinyanForm(request.POST)
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            minyan_name = form.cleaned_data['name']
            minyan = Minyan.objects.create(name=minyan_name)
            return render(request, 'minyan_mailer/sign_up.html', {'minyan': minyan})

    return render(request, 'minyan_mailer/index.html', {
        'form': form,
    })


def login(request):
    uname = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=uname, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)
        else:
            msg = 'Account disabled, sorry!'
    else:
        msg = 'invalid login'

def minyan_sign_up(request):
    '''
    minyan = get_object_or_404(Minyan, pk=minyan_id)

    davenings = minyan.davening_set.all()

    print(davenings)

    return render(request, 'minyan_mailer/sign_up.html', {'minyan': minyan})
    '''
    if request.method == 'GET':
        gabbai_form = UserForm()
        form = MinyanForm()
    else:
        gabbai_form = UserForm(request.POST)
        if gabbai_form.is_valid():
            gabbai_username = gabbai_form.cleaned_data['username']
            gabbai_email = gabbai_form.cleaned_data['email']
            gabbai_pass = gabbai_form.cleaned_data['password']

            new_gabbai = User.objects.create_user(username=gabbai_username, email=gabbai_email, password=gabbai_pass)
            gabbai_group = Group.objects.get(name='Gabbai')

            gabbai_group.user_set.add(new_gabbai)

        form = MinyanForm(request.POST)
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid() and new_gabbai:
            minyan_name = form.cleaned_data['name']
            minyan = Minyan.objects.create(name=minyan_name, gabbai=new_gabbai)
            return render(request, 'minyan_mailer/gabbai_home.html', {'gabbai': new_gabbai})

    return render(request, 'minyan_mailer/sign_up.html', {'gabbai_form': gabbai_form,
        'form': form,
    })


@login_required
def gabbai_home(request):

    #user = get_object_or_404(User, pk=gabbai_id)

    return render(request, 'minyan_mailer/gabbai_home.html')

def new_davening(request, minyan_id):
    if request.method == 'GET':
        form = DaveningForm()
    else:
        form = DaveningForm(request.POST)
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            davening_title = form.cleaned_data['title']
            davening_minyan = get_object_or_404(Minyan, pk=minyan_id)
            davening_day_of_week = form.cleaned_data['day_of_week']
            davening_group = form.cleaned_data['group']
            davening = Davening.objects.create(title=davening_title,
                                               minyan=davening_minyan,
                                               day_of_week=davening_day_of_week,
                                               group=davening_group,
            )
            return render(request, 'minyan_mailer/index.html')

    return render(request, 'minyan_mailer/new_davening.html', {
        'form': form,
    })
