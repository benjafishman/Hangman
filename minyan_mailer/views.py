from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from minyan_mailer.models import Minyan, Davening, Member
from minyan_mailer.forms import MinyanForm, UserForm, User, DaveningForm
# Create your views here.


def index(request):
    return render(request, 'minyan_mailer/index.html')

@login_required
def minyan_create(request):
    if request.method == 'GET':
        minyan_form = MinyanForm()
    else:
        minyan_form = MinyanForm(request.POST)
        member = Member.objects.get(user=request.user)
        # If data is valid, proceeds to create a new minyan and redirect the user
        if minyan_form.is_valid():
            minyan_name = minyan_form.cleaned_data['name']
            minyan_email = minyan_form.cleaned_data['contact_email']

            # Create the Minyan
            minyan = Minyan.objects.create(name=minyan_name, gabbai=member, contact_email=minyan_email)

            # Add new minyan to users set of minyans
            member.minyans.add(minyan)
            return HttpResponseRedirect(reverse('minyan_mailer:user_profile'))

    return render(request, 'minyan_mailer/minyan_create.html', {
        'form': minyan_form,
    })


@login_required
def user_profile(request):
    print(request.user)
    # get all minyans associated with this user
    member = Member.objects.get(user=request.user)

    print(member)

    minyans = member.minyans.all()

    print(minyans)

    return render(request, 'minyan_mailer/user_profile.html', {'minyans': minyans})

def minyan_profile(request, minyan_id):
    minyan = Minyan.objects.get(pk=minyan_id)
    print('here')
    davenings = minyan.davening_set.all()

    print(davenings)

    return render(request, 'minyan_mailer/minyan_profile.html', {'davenings':davenings, 'minyan':minyan})


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

