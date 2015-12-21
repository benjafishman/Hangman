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
            return render(request, 'minyan_mailer/register.html', {'minyan': minyan})

    return render(request, 'minyan_mailer/index.html', {
        'form': form,
    })

def minyan_register(request):
    if request.method == 'GET':
        # add form to register new user/gabbai
        if not request.user.is_authenticated():
            gabbai_form = UserForm()
        else:
            gabbai_form = None

        minyan_form = MinyanForm()
    else:
        if not request.user.is_authenticated():
            gabbai_form = UserForm(request.POST)
            if gabbai_form.is_valid():
                gabbai_username = gabbai_form.cleaned_data['username']
                gabbai_email = gabbai_form.cleaned_data['email']
                gabbai_pass = gabbai_form.cleaned_data['password']

                new_gabbai = User.objects.create_user(username=gabbai_username, email=gabbai_email, password=gabbai_pass)
                gabbai_group = Group.objects.get(name='Gabbai')
                gabbai_group.user_set.add(new_gabbai)
                # log a user in
                new_gabbai = authenticate(username=gabbai_username, password=gabbai_pass)
                gabbai = new_gabbai

                login(request, gabbai)
        else:
            gabbai=request.user
            print(gabbai.username)

        minyan_form = MinyanForm(request.POST)
        # If data is valid, proceeds to create a new post and redirect the user
        if minyan_form.is_valid() and gabbai:
            minyan_name = minyan_form.cleaned_data['name']
            print(gabbai.username)
            print("here1")
            minyan = Minyan.objects.create(name=minyan_name, user=gabbai)
            print("here2")

            return HttpResponseRedirect(reverse('minyan_mailer:gabbai_home'))

    return render(request, 'minyan_mailer/register.html', {'gabbai_form': gabbai_form,
        'form': minyan_form,
    })


@login_required
def gabbai_home(request):

    #user = get_object_or_404(User, pk=gabbai_id)

    print(request.user.username)

    # get all minyans associated with this user
    minyans = Minyan.objects.filter(user=request.user)

    print(minyans)

    return render(request, 'minyan_mailer/gabbai_home.html', {'minyans': minyans})

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
