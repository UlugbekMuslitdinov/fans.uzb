from django.db import models

from shop.models import Product
# Create your models here.


class Order (models.Model):
    first_name = models.CharField("Ism", max_length=60)
    last_name = models.CharField("Familiya", max_length=60)
    phone_number = models.CharField("Telefon raqami", max_length=13, null=True)
    email = models.EmailField("Elektron pochta", null=True, blank=True)
    address = models.CharField("Manzil", max_length=150)
    postal_code = models.CharField("Pochta indeksi", max_length=30)
    city = models.CharField("Shahar", max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField("To'langan", default=False)  # оплачен ли заказ

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Buyurtma'
        verbose_name_plural = 'Buyurtmalar'

    def __str__(self):
        return 'Заказ {}'.format(self.id)

    def get_total_cost(self):
        # общая сумма заказа
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField("Narx", max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField("Ko'pligi", default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

