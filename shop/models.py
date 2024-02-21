from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Категория')
    slug = models.SlugField(max_length=20, db_index=True, verbose_name='слаг')

    objects = models.Manager()

    def __str__(self):
        return f'{self.title}'


class Product(models.Model):

    class IN_STOCK(models.TextChoices):
        YES = 'YES', 'В наличии'
        NO = 'NO', 'Нет в наличии'

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category', verbose_name='Категория')
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=20, verbose_name='слаг')
    description = models.TextField(max_length=500, verbose_name='Описание')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to='products/%Y/%m/%d', verbose_name='Изображение')
    in_stock = models.CharField(max_length=3, choices=IN_STOCK.choices, default=IN_STOCK.NO, verbose_name='Статус')
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
