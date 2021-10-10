from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from apps.restaurants.models import Dish
from apps.users.models import Profile


class OrderStatus(models.TextChoices):
    NEW = 'new', 'New'
    WAITING = 'waiting', 'Waiting'
    READY = 'ready', 'Ready'
    DELIVERED = 'delivered', 'Delivered'
    ACCEPTED = 'accepted', 'Accepted'
    REJECTED = 'rejected', 'Rejected'


class Order(MPTTModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    parent = TreeForeignKey('self', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, default=OrderStatus.NEW, choices=OrderStatus.choices)

    class Meta:
        db_table = 'orders'

    def __str__(self):
        return f'Order # {self.id}'


class OrderItem(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, null=True, on_delete=models.SET_NULL)
    dish_price = models.DecimalField(max_digits=10, decimal_places=2)
    dish_name = models.CharField(max_length=250)
    dish_quantity = models.IntegerField(default=1)

    class Meta:
        db_table = 'order_items'

    def __str__(self):
        return f'Order # {self.id} - Dish {self.dish_name}'
