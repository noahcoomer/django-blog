from django.contrib import admin
from .models import Blog, Category, Author, Comment

class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {}


admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Comment)