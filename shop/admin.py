from django.contrib import admin

from .models import Category, Product, Order, OrderProduct


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


class OrderItemsInline(admin.TabularInline):
    model = OrderProduct
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'email', 'created', 'get_total_cost']
    list_filter = ['created', 'paid']
    inlines = [OrderItemsInline]

