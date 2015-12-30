from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from minyan_mailer.models import Minyan, Davening, Member, Davening_Group, Mailing
from minyan_mailer.forms import MinyanForm, UserForm, User, DaveningForm, UnauthenticatedDaveningSignUpForm

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseForbidden

from minyan_mailer.api_wrappers.MailGunWrapper import MailGunWrapper
from minyan_mailer.tasks import add



# Create your views here.


def index(request):
    return render(request, 'minyan_mailer/index.html')


@login_required
def user_profile(request):
    print(request.user)
    # get all minyans associated with this user
    member = Member.objects.get(user=request.user)

    print(member)

    minyans = member.minyans.all()

    print(minyans)

    return render(request, 'minyan_mailer/user_profile.html', {'minyans': minyans})


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

            # Add permissions to member for this minyan
            content_type = ContentType.objects.get_for_model(Minyan)

            # Add new minyan to users set of minyans
            member.minyans.add(minyan)
            return HttpResponseRedirect(reverse('minyan_mailer:user_profile'))

    return render(request, 'minyan_mailer/minyan_create.html', {
        'form': minyan_form,
    })


def minyan_profile(request, minyan_id):
    minyan = Minyan.objects.get(pk=minyan_id)
    davenings = minyan.davening_set.all()

    is_gabbai = False

    if request.user.is_authenticated():
        member = Member.objects.get(user=request.user)
        is_gabbai = member.is_gabbai(minyan)

    print(is_gabbai)

    return render(request, 'minyan_mailer/minyan_profile.html',
                  {'davenings': davenings, 'minyan': minyan,'is_gabbai': is_gabbai})


@login_required
def davening_create(request, minyan_id):
    # if the user is not the gabbai of the specific minyan
    # then they can not create any davening
    member = Member.objects.get(user=request.user)
    minyan = get_object_or_404(Minyan, pk=minyan_id)
    if member.is_gabbai(minyan):
        if request.method == 'GET':
            form = DaveningForm()
        else:

            form = DaveningForm(request.POST)
            # If data is valid, proceeds to create a new post and redirect the user
            if form.is_valid():
                davening_title = form.cleaned_data['title']
                davening_time = form.cleaned_data['davening_time']
                davening_days = form.cleaned_data['days']
                davening_email_time = form.cleaned_data['email_time']
                print(davening_days)

                # Create the davening group real quick
                davening_group_title = davening_title.replace(" ", "_") + '_davening_group'
                davening_group = Davening_Group.objects.create(title=davening_group_title, minyan=minyan, mailing_list_title=davening_group_title)
                davening_group.save()
                # add the davening group to the davening



                davening = Davening.objects.create(title=davening_title,
                                                   minyan=minyan,
                                                   davening_time=davening_time,
                                                   days=davening_days,
                                                   email_time = davening_email_time,
                                                   primary_davening_group=davening_group,
                )

                #davening.primary_davening_group.add(davening_group)

                # we also will create a mailgun related lsit for this davening group
                MailGun = MailGunWrapper()
                mailgun_request = MailGun.create_mailing_list(davening_group_title)

                print(mailgun_request)

                return HttpResponseRedirect(reverse('minyan_mailer:davening_profile', args=(davening.id,)))

        return render(request, 'minyan_mailer/davening_create.html', {
            'form': form,
        })
    else:
        return HttpResponseForbidden()


def davening_profile(request, davening_id):
    # todo: going to need to types of forms here:
    # ## 1. Authenticated form with radio button and just use user object
    # ## 2. Unauthenticated user form with text input

    davening = Davening.objects.get(pk=davening_id)

    is_gabbai = False

    if request.user.is_authenticated():
        member = Member.objects.get(user=request.user)
        is_gabbai = member.is_gabbai(davening.minyan)

    print(davening.days)

    if request.method == 'GET':
        unauthenticated_user_form = UnauthenticatedDaveningSignUpForm()
    else:
        unauthenticated_user_form = UnauthenticatedDaveningSignUpForm(request.POST)
        if unauthenticated_user_form.is_valid():
            # grab input
            # create mailing object with email data
            # set davening_group to group associated with the current davening
            # add the email to the mailgun mailing list
            email = unauthenticated_user_form.cleaned_data['email']
            print(email)
            print(davening.id)
            davening_group = Davening_Group.objects.get(title=davening.title.replace(" ", "_")+'_davening_group')
            print(davening_group)
            mailing = Mailing.objects.create(email=email,davening_group=davening_group)

            # send user info to MailGun List
            MG = MailGunWrapper()
            mailgun_request = MG.add_list_member(davening_group.title,email)
            print(mailgun_request)

            #add.delay(2, 2)

            #print("scheduled add???")
            return HttpResponseRedirect(reverse('minyan_mailer:davening_profile', args=(davening.id,)) + '?submit=true')


    print(davening)
    return render(request, 'minyan_mailer/davening_profile.html', {'davening': davening, 'sign_up_form': unauthenticated_user_form, 'is_gabbai': is_gabbai})
