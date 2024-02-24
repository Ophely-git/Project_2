from decimal import Decimal
from django.conf import settings
from .models import Product


class Cart:

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, override_quantity=False):
        product_pk = str(product.pk)
        if product_pk not in self.cart:
            self.cart[product_pk] = {'quantity': 0, 'price': str(product.price)}
        if override_quantity:
            self.cart[product_pk]['quantity'] = quantity
        else:
            self.cart[product_pk]['quantity'] += quantity

        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product):
        product_pk = str(product.pk)
        if product_pk in self.cart:
            del self.cart[product_pk]
            self.save()

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def __iter__(self):
        product_list_id = self.cart.keys()
        products = Product.objects.filter(pk__in=product_list_id)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.pk)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def cart_count(self):
        product_list_id = self.cart.keys()
        products = Product.objects.filter(pk__in=product_list_id)
        count = products.count()
        return count
