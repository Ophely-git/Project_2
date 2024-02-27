from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.decorators.http import require_POST
from django.db.models import Q

from .models import Category, Product, Order, OrderProduct
from .cart import Cart
from .forms import CartAddProductForm, OrderForm


# Shop pages
def homepage(request, category_slug=None):
    categories = get_list_or_404(Category)
    products = get_list_or_404(Product)
    category = None

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products,
    }
    return render(request, 'shop/homepage.html', context)


def product_detail(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    add_product_form = CartAddProductForm()
    context = {
        'product': product,
        'add_product_form': add_product_form
    }
    return render(request, 'shop/product_detail.html', context)


# Cart pages

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'override': True
        })

    context = {
        'cart': cart,
    }
    return render(request, 'shop/cart_detail.html', context)


@require_POST
def cart_add(request, product_pk):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_pk, in_stock=Product.In_stock.YES)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['quantity'])

    return redirect('shop:product_detail', product.slug)


def cart_remove(request, product_pk):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_pk)
    cart.remove(product)
    return redirect('shop:cart_detail')


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderProduct.objects.create(order=order,
                                            product=item['product'],
                                            price=item['price'],
                                            quantity=item['quantity'])
            cart.clear()
            context = {
                'order': order,
            }
            return render(request, 'shop/order_created.html', context)
    else:
        form = OrderForm()
    context = {
        'cart': cart,
        'form': form,
    }
    return render(request, 'shop/order_create.html', context)


def search(request):
    if request.method == 'POST':
        def_search = request.POST.get('search')
        products = Product.objects.filter(Q(name__icontains=def_search))
        context = {
            'products': products,
            'def_search': def_search
        }
        return render(request, 'shop/search.html', context)

