from django.db import models
from django.shortcuts import reverse
from PIL import Image


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Категория')
    slug = models.SlugField(max_length=20, db_index=True, verbose_name='слаг')

    objects = models.Manager()

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('shop:list_by_category', args=[self.slug])


class Product(models.Model):

    class In_stock(models.TextChoices):
        YES = 'YES', 'В наличии'
        NO = 'NO', 'Нет в наличии'

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category', verbose_name='Категория')
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=20, verbose_name='слаг')
    description = models.TextField(max_length=500, verbose_name='Описание')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to='products/%Y/%m/%d', verbose_name='Изображение')
    in_stock = models.CharField(max_length=3, choices=In_stock.choices, default=In_stock.NO, verbose_name='Статус')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    objects = models.Manager()

    class Meta:
        ordering = ['-updated']
        indexes = [
            models.Index(fields=['-updated']),
            models.Index(fields=['slug'])
        ]

    def __str__(self):
        return f'{self.category}, {self.name}, {self.in_stock}, {self.updated}'

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        super().save()  # saving image first

        img = Image.open(self.image.path) # Open image using self

        if img.height > 300 or img.width > 300:
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(self.image.path)  # saving image at the same path


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name}, {self.email}, {self.created}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    price = models.PositiveIntegerField(default=1)
    quantity = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return f'{self.order}, {self.product}, {self.product}, {self.quantity}'

    def get_cost(self):
        return self.price * self.quantity