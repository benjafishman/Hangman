from django.contrib import admin

# Register your models here.
from minyan_mailer.models import Mailing,Minyan,Davening, Davening_Group, Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ['user']

class MinyanAdmin(admin.ModelAdmin):
    list_display = ['name','created', 'gabbai']

class Davening_GroupInline(admin.TabularInline):
    model = Davening_Group
    extra = 3

class DaveningAdmin(admin.ModelAdmin):
    list_display = ['title', 'day_of_week', 'davening_time', 'minyan']

class Davening_GroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'minyan']

class MailingAdmin(admin.ModelAdmin):
    list_display = ['davening_group','email']

admin.site.register(Member, MemberAdmin)
admin.site.register(Minyan, MinyanAdmin)
admin.site.register(Davening, DaveningAdmin)
admin.site.register(Davening_Group, Davening_GroupAdmin)
admin.site.register(Mailing, MailingAdmin)