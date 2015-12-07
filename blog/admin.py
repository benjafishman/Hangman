from django.contrib import admin
# Register your models here.

from blog.models import GemaraPost, Category, Section, Mesechta, Gemara, Statement, Person

'''
class ChallengeInline(admin.TabularInline):
    model = Challenge
    extra = 3
'''

class StatementInline(admin.TabularInline):
    model = Statement
    extra = 3

class GemaraPostAdmin(admin.ModelAdmin):

    list_display = ['title', 'description','get_categories']
    list_filter = ['published', 'created']
    search_fields = ['title', 'description', 'content']

    inlines = [StatementInline]

    date_heirarchy = 'created'
    save_on_top = True
    prepopulated_fields = {'slug': ('title',)}
    '''
    fieldsets = [
        (None,               {'fields': ['title', 'description']}),
        ('Date information', {'fields': ['published']}),
    ]
    date_heirarchy = 'created'
    save_on_top = True
    prepopulated_fields = {'slug': ('title',)}
    '''




class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']

class SectionAdmin(admin.ModelAdmin):
    list_display = ['title']

class MesechtaAdmin(admin.ModelAdmin):
    list_display = ['get_seder_display']

class GemaraAdmin(admin.ModelAdmin):
    list_display = ['title','seder','number_of_perakim','number_of_daf']

class PersonAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(GemaraPost,GemaraPostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Mesechta, MesechtaAdmin)
admin.site.register(Gemara, GemaraAdmin)
admin.site.register(Person, PersonAdmin)
