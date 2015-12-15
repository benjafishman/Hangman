from django.contrib import admin

# Register your models here.
from minyan_mailer.models import Minyan, Davening

class MinyanAdmin(admin.ModelAdmin):
    list_display = ['name', 'created']

class DaveningAdmin(admin.ModelAdmin):
    list_display = ['title','day_of_week','davening_time']


admin.site.register(Minyan,MinyanAdmin)
admin.site.register(Davening, DaveningAdmin)