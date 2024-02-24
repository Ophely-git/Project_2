from django.urls import path, include

from .views import homepage, product_detail, cart_add, cart_detail, cart_remove, order_create, search

app_name='shop'

urlpatterns = [
    path('cart/', cart_detail, name='cart_detail'),
    path('cart/add/<int:product_pk>/', cart_add, name='cart_add'),
    path('order/', order_create, name='order_create'),
    path('search/', search, name='search'),
    path('', homepage, name='homepage'),
    path('<slug:category_slug>/', homepage, name='list_by_category'),
    path('detail/<slug:product_slug>/', product_detail, name='product_detail'),
    path('remove/<int:product_pk>', cart_remove, name='cart_remove'),



]

