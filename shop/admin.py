from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'updated', 'in_stock']
    search_fields = ['name', 'description']
    list_editable = ['price', 'in_stock']
    list_filter = ['in_stock', 'created', 'updated']
    prepopulated_fields = {'slug': ('name', )}