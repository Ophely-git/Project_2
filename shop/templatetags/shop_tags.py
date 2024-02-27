from django import template
from django.db.models import Count

from ..models import Category, Product

register = template.Library()


@register.inclusion_tag('system/category_list.html')
def category_list():
    categories = Category.objects.all()
    return {'categories': categories}


@register.simple_tag
def newest_products(count=10):
    return Product.objects.filter(in_stock=Product.In_stock.YES).order_by('-updated')[:count]


@register.simple_tag
def popular_products(count=10):
    product = Product.objects.filter(in_stock=Product.In_stock.YES)
    return product.annotate(total_count=Count('order_items')).order_by('-total_count')[:count]