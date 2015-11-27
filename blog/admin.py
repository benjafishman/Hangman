from django.contrib import admin
# Register your models here.

from blog.models import Post, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'get_categories']
    list_filter = ['published', 'created']
    search_fields = ['title', 'description', 'content']
    date_heirarchy = 'created'
    save_on_top = True
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Post,PostAdmin)
admin.site.register(Category, CategoryAdmin)
