from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404

from .models import Category, Product


def homepage(request):
    category = get_list_or_404(Category)
    products = get_list_or_404(Product)
    context = {
        'category': category,
        'products' : products,
    }
    return render(request, 'shop/homepage.html', context)



