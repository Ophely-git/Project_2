from .cart import Cart


# Отображение корзины на всех страницах
def cart(request):
    return {'cart': Cart(request)}
