from django.contrib import admin

# Register your models here.
from minyan_mailer.models import Minyan, Davening, Davening_Group


class MinyanAdmin(admin.ModelAdmin):
    list_display = ['name', 'user','created']

class Davening_GroupInline(admin.TabularInline):
    model = Davening_Group
    extra = 3

class DaveningAdmin(admin.ModelAdmin):
    list_display = ['title', 'day_of_week', 'davening_time']
    #inlines = [Davening_GroupInline]

class Davening_GroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'email']


admin.site.register(Minyan, MinyanAdmin)
admin.site.register(Davening, DaveningAdmin)
admin.site.register(Davening_Group, Davening_GroupAdmin)