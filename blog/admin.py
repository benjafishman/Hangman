from django.contrib import admin
# Register your models here.

from blog.models import GemaraPost, Category, Section, \
    Gemara, Statement, Person, ParshaPost, Chumash, \
    Parsha, ParshaQuestion
'''
class ChallengeInline(admin.TabularInline):
    model = Challenge
    extra = 3


class StatementInline(admin.TabularInline):
    model = Statement
    extra = 0

class GemaraPostAdmin(admin.ModelAdmin):

    list_display = ['title', 'description','get_categories']
    list_filter = ['published', 'created']
    search_fields = ['title', 'description', 'content']

    inlines = [StatementInline]

    date_heirarchy = 'created'
    save_on_top = True
    prepopulated_fields = {'slug': ('title',)}


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

'''

class ParshaPostAdmin(admin.ModelAdmin):

    list_display = ['title', 'description','get_categories']
    list_filter = ['published', 'created']
    search_fields = ['title', 'description', 'content']
    date_heirarchy = 'created'
    save_on_top = True
    prepopulated_fields = {'slug': ('title',)}

class ParshaQuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'parsha']
    list_filter = ['created']
    date_heirarchy = 'created'
    save_on_top = True

class ChumashAdmin(admin.ModelAdmin):
    list_display = ['title']

class ParshaAdmin(admin.ModelAdmin):
    list_display = ['eng_name', 'sefer']
    search_fields = ['eng_name', 'sefer']

admin.site.register(Parsha, ParshaAdmin)
admin.site.register(ParshaQuestion, ParshaQuestionAdmin)
admin.site.register(Chumash, ChumashAdmin)