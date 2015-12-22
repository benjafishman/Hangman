from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from minyan_mailer.models import Minyan, Davening
from minyan_mailer.forms import MinyanForm, UserForm, User, DaveningForm
# Create your views here.


def index(request):
    print(request)
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
        # If there is no user we will show the gabbai/new user form
        # so they create a user associated with the minyan
        if not request.user.is_authenticated():
            gabbai_form = UserForm(request.POST)
            if gabbai_form.is_valid():
                # get user input from form and validate it
                gabbai_username = gabbai_form.cleaned_data['username']
                gabbai_email = gabbai_form.cleaned_data['email']
                gabbai_pass = gabbai_form.cleaned_data['password']

                # create new user model
                new_gabbai = User.objects.create_user(username=gabbai_username, email=gabbai_email, password=gabbai_pass)
                gabbai_group = Group.objects.get(name='Gabbai')
                gabbai_group.user_set.add(new_gabbai)

                # authenitcate/log user in
                new_gabbai = authenticate(username=gabbai_username, password=gabbai_pass)
                gabbai = new_gabbai
                login(request, gabbai)
        else:
            # A user already logged in
            gabbai=request.user
            #print(gabbai.username)

        # the minyan form will always be displayed
        minyan_form = MinyanForm(request.POST)

        # If data is valid, proceeds to create a new minyan and redirect the user
        if minyan_form.is_valid() and gabbai:
            minyan_name = minyan_form.cleaned_data['name']
            minyan = Minyan.objects.create(name=minyan_name, user=gabbai)
            return HttpResponseRedirect(reverse('minyan_mailer:user_profile'))

    return render(request, 'minyan_mailer/register.html', {'gabbai_form': gabbai_form,
        'form': minyan_form,
    })


@login_required
def user_profile(request):
    # get all minyans associated with this user
    minyans = Minyan.objects.filter(user=request.user)

    return render(request, 'minyan_mailer/user_profile.html', {'minyans': minyans})

def minyan_detail(request, minyan_id):
    minyan = Minyan.objects.get(pk=minyan_id)
    print('here')
    davenings = minyan.davening_set.all()

    print(davenings)

    return render(request, 'minyan_mailer/minyan_detail.html', {'davenings':davenings, 'minyan':minyan})


@login_required
def new_davening(request, minyan_id):
    if request.method == 'GET':
        form = DaveningForm()
    else:
        davening_minyan = get_object_or_404(Minyan, pk=minyan_id)
        form = DaveningForm(request.POST)
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            davening_title = form.cleaned_data['title']
            davening_day_of_week = form.cleaned_data['day_of_week']
            davening_time = form.cleaned_data['davening_time']
            davening_group = form.cleaned_data['group']
            davening = Davening.objects.create(title=davening_title,
                                               minyan=davening_minyan,
                                               davening_time=davening_time,
                                               day_of_week=davening_day_of_week,
                                               group=davening_group,
            )
            return HttpResponseRedirect(reverse('minyan_mailer:davening'))

    return render(request, 'minyan_mailer/new_davening.html', {
        'form': form,
    })

def davening_detail(request, davening_id):
    davening = Davening.objects.get(pk=davening_id)
    print(davening)
    return render(request, 'minyan_mailer/davening_detail.html', {'davening':davening})

