from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from minyan_mailer.models import Minyan, Davening, Member, Davening_Group, PeriodicMailing
from minyan_mailer.forms import MinyanForm, UserForm, User, DaveningForm, UnauthenticatedDaveningSignUpForm, \
    PeriodicMailingForm

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseForbidden

from minyan_mailer.api_wrappers.MailGunWrapper import MailGunWrapper
from minyan_mailer.tasks import add
import pytz
from datetime import datetime, date

# celery imports
from djcelery.models import CrontabSchedule, PeriodicTask

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

    # temporary: created a numbered list of minyans
    # user is gabbai of to display on front end
    member_minyans = {m: 0 for m in minyans}
    print(member_minyans)
    for m in minyans:
        print(m)
        if member.is_gabbai(m):
            member_minyans[m] = 1

    print(member_minyans)

    print(minyans)

    return render(request, 'minyan_mailer/user_profile.html', {'minyans': member_minyans})


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

    print(minyan.timezone)

    is_gabbai = False

    if request.user.is_authenticated():
        member = Member.objects.get(user=request.user)
        is_gabbai = member.is_gabbai(minyan)

    print(is_gabbai)

    return render(request, 'minyan_mailer/minyan_profile.html',
                  {'davenings': davenings, 'minyan': minyan, 'is_gabbai': is_gabbai})


@login_required
def davening_create(request, minyan_id):
    # if the user is not the gabbai of the specific minyan
    # then they can not create any davening
    member = Member.objects.get(user=request.user)
    minyan = get_object_or_404(Minyan, pk=minyan_id)

    if member.is_gabbai(minyan):
        if request.method == 'GET':
            form = DaveningForm()
            periodic_mailing_form = PeriodicMailingForm()
        else:
            form = DaveningForm(request.POST)
            periodic_mailing_form = PeriodicMailingForm(request.POST)
            # periodic_mailing_form = PeriodicMailingForm(request.POST)
            # If data is valid, proceeds to create a new post and redirect the user
            if form.is_valid():
                davening_title = form.cleaned_data['title']
                davening_time = form.cleaned_data['local_davening_time']
                davening_days = form.cleaned_data['days']

                # Create the davening group real quick
                davening_group_title = davening_title.replace(" ", "_") + '_davening_group'
                davening_group = Davening_Group.objects.create(title=davening_group_title, minyan=minyan,
                                                               mailing_list_title=davening_group_title)
                davening_group.save()

                #TODO: add below back at some point
                davening = Davening.objects.create(title=davening_title,
                                                   minyan=minyan,
                                                   local_davening_time=davening_time,
                                                   days=davening_days,
                                                   primary_davening_group=davening_group,
                )


                #TODO: remove de-comment below code when ready
                #davening.primary_davening_group.add(davening_group)
                # we also will create a mailgun related list for this davening (group)
                '''
                MailGun = MailGunWrapper()
                mailgun_request = MailGun.create_mailing_list(davening_group_title)
                print(mailgun_request)
                '''

                # If user has opted to set up a mailing proceed with mailing creation
                #TODO: Somehow check if user set any of this
                if periodic_mailing_form.is_valid():
                    email_text = periodic_mailing_form.cleaned_data['email_text']
                    print(email_text)

                    send_days = periodic_mailing_form.cleaned_data['send_days']
                    print(send_days)

                    mailing_send_time = periodic_mailing_form.cleaned_data['email_local_send_time']
                    print(mailing_send_time)

                    mailing_enabled = periodic_mailing_form.cleaned_data['enabled']
                    print(mailing_enabled)

                    '''
                    Need to create or associate a
                    crontab schedule with this minyan

                    e.x. of creating a crontab object:
                    ct = CT.objects.create(minute=59,hour=3,day_of_week=3)
                    0. Convert user input to utc
                    1. Create a crontab with time and day:
                        1a. parse user input of email time
                        1b: day_of_week(s) flatten list seperated by comma
                    2. get the crontab id
                    3. Create a periodicTask with id of the crontab from above
                        3a. example of periodicTask is: p = PeriodicTask.objects.create(name='test from shell 1',task='minyan_mailer.tasks.send_test_list_email',crontab_id=7)
                    '''

                    utc_email_time = convert_to_utc(minyan.timezone, mailing_send_time)

                    print('UTC Email time is', utc_email_time)

                    # Pull out hour and minute for crontab
                    ct_hour = utc_email_time.hour
                    ct_minute = utc_email_time.minute

                    # flatten list seperated by comma
                    ct_days = ','.join(davening_days)

                    # We have to increment each day if utc time happens to be in the following day
                    # had to mod 7 for the case of user input of day 6 (saturday) then incremented by one (7) should map to day 0
                    if day_checker(utc_email_time, davening.local_davening_time):
                        incremented_days = [str((int(x) + 1) % 7) for x in davening_days]
                        ct_days = ','.join(incremented_days)

                    crontab_dic = {'hour': ct_hour, 'minute': ct_minute, 'day_of_week': ct_days}

                    # If crontab exists set the pre-existing crontab id to the current crontab request
                    ct_id = crontab_exists(crontab_dic)

                    # If crontab does not exist create a new one
                    if not ct_id:
                        print('Creating new crontab')
                        crontab = CrontabSchedule.objects.create(minute=ct_minute, hour=ct_hour, day_of_week=ct_days)
                        ct_id = crontab.id

                    print('crontab id: ', ct_id)
                    # create the periodic task with the above crontab id

                    # Set the name of the task
                    task_name = davening_title + '_periodic_email'
                    pt = PeriodicTask.objects.create(name=task_name, task='minyan_mailer.tasks.send_test_list_email',
                                                     crontab_id=ct_id, enabled=mailing_enabled)

                    # Now we create the PeriodicMailing object
                    pm = PeriodicMailing.objects.create(email_text=email_text, enabled=mailing_enabled,
                                                        mailgun_list_name='Test_MailGun_List',
                                                        crontab_schedule_id=ct_id, periodic_task_id=pt.id, email_local_send_time=mailing_send_time,
                                                        email_utc_send_time=utc_email_time, davening_key=davening)
                    print(pt)

                return HttpResponseRedirect(reverse('minyan_mailer:davening_profile', args=(davening.id,)))

        return render(request, 'minyan_mailer/davening_create.html', {
            'form': form, 'periodic_mailing_form': periodic_mailing_form,
        })
    else:
        return HttpResponseForbidden()


def davening_profile(request, davening_id):
    # todo: going to need to types of forms here:
    # ## 1. Authenticated form with radio button and just use user object
    # ## 2. Unauthenticated user form with text input

    davening = Davening.objects.get(pk=davening_id)

    is_gabbai = False

    utc_time = convert_to_utc(davening.minyan.timezone, davening.local_davening_time)

    if request.user.is_authenticated():
        member = Member.objects.get(user=request.user)
        is_gabbai = member.is_gabbai(davening.minyan)

    # print(davening.days)

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
            davening_group = Davening_Group.objects.get(title=davening.title.replace(" ", "_") + '_davening_group')

            # send user info to MailGun List
            MG = MailGunWrapper()
            mailgun_request = MG.add_list_member(davening_group.title, email)
            print(mailgun_request)
            return HttpResponseRedirect(reverse('minyan_mailer:davening_profile', args=(davening.id,)) + '?submit=true')

    print(davening)
    return render(request, 'minyan_mailer/davening_profile.html',
                  {'davening': davening, 'sign_up_form': unauthenticated_user_form, 'is_gabbai': is_gabbai})


@login_required
# TODO:FINISH THIS VIEW
def periodic_mailing_create(request, davening_id):
    davening = Davening.objects.get(pk=davening_id)
    member = Member.objects.get(user=request.user)
    # deny access to non gabbai
    if not member.is_gabbai(davening.minyan):
        return HttpResponseForbidden()
    # So you're the gabbai ey?
    # fine we will let you create a peridic email
    # periodic email form?

    return False

@login_required
def periodic_mailing_edit(request, periodic_mailing_id):
    print('mailing edit')
    mailing = PeriodicMailing.objects.get(pk=periodic_mailing_id)
    # TODO: should checking if the user is gabbai process be function?
    member = Member.objects.get(user=request.user)

    davening = mailing.davening_key
    days = CrontabSchedule.objects.get(pk=mailing.crontab_schedule_id).day_of_week
    print(type(days))
    print(days.split(","))
    is_gabbai = False
    if request.user.is_authenticated():
        member = Member.objects.get(user=request.user)
        is_gabbai = member.is_gabbai(davening.minyan)

    if is_gabbai:
        if request.method == 'GET':
            form = PeriodicMailingForm(instance=mailing)
            form.fields["send_days"].initial = days
        else:
            form = PeriodicMailingForm(request.POST, instance=mailing)
            if form.is_valid():  #is_valid is function not property
                if form.has_changed():
                    print('form changed')
                    print("The following fields changed: %s" % ", ".join(form.changed_data))
                    for d in form.changed_data:
                        print(d)
                        if d == 'email_local_send_time' or (d is 'send_days' and days.split(",") != form.cleaned_data['send_days']):
                            print('do time magic')
                            minyan = davening.minyan

                            utc_email_time = convert_to_utc(minyan.timezone, form.cleaned_data['email_local_send_time'])

                            print('UTC Email time is', utc_email_time)

                            # Pull out hour and minute for crontab
                            ct_hour = utc_email_time.hour
                            ct_minute = utc_email_time.minute

                            # flatten list seperated by comma
                            ct_days = ','.join(form.cleaned_data['send_days'])

                            # We have to increment each day if utc time happens to be in the following day
                            # had to mod 7 for the case of user input of day 6 (saturday) then incremented by one (7) should map to day 0
                            if day_checker(utc_email_time, form.cleaned_data['email_local_send_time']):
                                incremented_days = [str((int(x) + 1) % 7) for x in form.cleaned_data['send_days']]
                                ct_days = ','.join(incremented_days)

                            crontab_dic = {'hour': ct_hour, 'minute': ct_minute, 'day_of_week': ct_days}

                            # If crontab exists set the pre-existing crontab id to the current crontab request
                            ct_id = crontab_exists(crontab_dic)

                            # If crontab does not exist create a new one
                            if not ct_id:
                                print('Creating new crontab')
                                crontab = CrontabSchedule.objects.create(minute=ct_minute, hour=ct_hour, day_of_week=ct_days)
                                ct_id = crontab.id

                            print('Crontab id', ct_id)
                            # since we created a new crontab
                            # we have to assign the cron tab id to the associated periodictask
                            pt = PeriodicTask.objects.get(pk=mailing.periodic_task_id)
                            print(pt)
                            pt.crontab_id = ct_id
                            pt.enabled = form.cleaned_data['enabled']
                            print(pt)
                            pt.save()
                            mailing.crontab_schedule_id = ct_id
                            mailing.d = form.cleaned_data[d]
                            if d is 'email_local_send_time':
                                mailing.email_utc_send_time = utc_email_time
                        elif d == 'enabled':
                            # set the periodic task enabled value to the value chosen by the user
                            pt = PeriodicTask.objects.get(pk=mailing.periodic_task_id)
                            pt.enabled = form.cleaned_data[d]
                            pt.save()
                        else:
                            mailing.d = form.cleaned_data[d]

                        mailing.save()
                        print('saved updates')

        return render(request, 'minyan_mailer/edit_mailing.html', {'mailing': mailing,
                                                                   'form': form})
    else:
        return HttpResponseForbidden()


def convert_to_utc(timezone, time):
    # TODO: timemzone/time validation
    '''
    :Helper function to convert a given time to its corresponding UTC time
    :param timezone: timezone variable
    :param time: time to convert to utc
    :return:
    '''
    d = date.today()
    # We need an entire date object so well combine the time with the current date
    # this might backfire
    convert = datetime.combine(d, time)

    print(type(convert))

    # tell pytz module which timezone were using
    local = pytz.timezone(timezone)

    # use pytz to localize the time
    local_time = local.localize(convert, is_dst=None)

    # conversion
    utc_dt = local_time.astimezone(pytz.utc)
    return utc_dt

def convert_to_local_time(timezone, time):
    print('utc time: ', time)
    print(timezone)
    d = date.today()
    # We need an entire date object so well combine the time with the current date
    # this might backfire
    convert = datetime.combine(d, time)
    print(convert)
    local_tz = pytz.timezone(timezone)
    print(local_tz)
    print(pytz.utc.localize(convert, is_dst=None).astimezone(local_tz))
    return convert.replace(tzinfo=pytz.utc).astimezone(local_tz)
    #print(pytz.utc.localize(time, is_dst=None).astimezone(timezone))


def day_checker(utc_time, local_time):
    # if utc-time is greater by a day update cron_dic_days by one (for each day)

    # create a timedelta of one day

    d = date.today()
    # We need an entire date object so well combine the time with the current date
    # this might backfire
    local_time = datetime.combine(d, local_time)

    if utc_time.date() > local_time.date():
        print('utc is greater')
        return True
    return False


def crontab_exists(cron_dic):
    '''
    Helper function to query if a user crontab schedule already exists.
    If it does then the id of the pre-existing crontab is returned
    If the crontab schedule is new, then the function returns fale
    :param cron_dic: dictionary holding cron info. e.x.: {'hour':hour,'minute':minute,'day_of_week':day(s)}
    :return: Pre-existing crontab id or False
    '''
    if CrontabSchedule.objects.filter(day_of_week=cron_dic['day_of_week'], hour=cron_dic['hour'],
                                      minute=cron_dic['minute']):
        print('Crontab exists')
        result = CrontabSchedule.objects.filter(day_of_week=cron_dic['day_of_week'], hour=cron_dic['hour'],
                                                minute=cron_dic['minute'])
        return result[0].id
    return False