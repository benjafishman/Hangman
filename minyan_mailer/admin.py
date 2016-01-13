from django.contrib import admin

# Register your models here.
from minyan_mailer.models import Minyan,Davening, Davening_Group, Member, PeriodicMailing
from kombu.transport.django import models as kombu_models

class MemberAdmin(admin.ModelAdmin):
    list_display = ['user']

class MinyanAdmin(admin.ModelAdmin):
    list_display = ['name','created', 'gabbai']

class Davening_GroupInline(admin.TabularInline):
    model = Davening_Group
    extra = 3

class DaveningAdmin(admin.ModelAdmin):
    list_display = [ 'minyan', 'title', 'days', 'davening_time', 'email_time', 'primary_davening_group', 'periodic_mailing' ]

class Davening_GroupAdmin(admin.ModelAdmin):
    list_display = ['minyan', 'title', 'mailing_list_title']

class PeriodicMailingAdmin(admin.ModelAdmin):
    list_display = ['email_text', 'enabled', 'mailgun_list_name', 'crontab_string', 'crontab_schedule_id', 'periodic_task_id', 'email_send_time']
admin.site.register(PeriodicMailing, PeriodicMailingAdmin)

admin.site.register(kombu_models.Message)
admin.site.register(Member, MemberAdmin)
admin.site.register(Minyan, MinyanAdmin)
admin.site.register(Davening, DaveningAdmin)
admin.site.register(Davening_Group, Davening_GroupAdmin)