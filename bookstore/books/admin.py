from django.contrib import admin
from .models import Category, Book
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'price', 'available']
    list_filter = ['available', 'category']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('title',)}