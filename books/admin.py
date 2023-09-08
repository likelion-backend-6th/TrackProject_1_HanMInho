from django.contrib import admin

from books.models import Category, Book


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'slug']
    list_filter = ['name']


@admin.register(Book)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'available', 'updated']
    list_filter = ['writer', 'available', 'created', 'updated']
    list_editable = ['available']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'writer', 'author']
