from django.db import models
from apps.restaurants.models import Dish, Restaurant
from apps.users.models import Profile


class OrderStatus(models.TextChoices):
    NEW = 'new', 'New'

    WAITING = 'waiting', 'Waiting'
    IN_PROCESS = 'in process', 'In process'
    READY = 'ready', 'Ready'

    ON_THE_WAY = 'on the way', 'On the way'
    DELIVERED = 'delivered', 'Delivered'

    ACCEPTED = 'accepted', 'Accepted'
    REJECTED = 'rejected', 'Rejected'


class Order(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=25, default=OrderStatus.NEW, choices=OrderStatus.choices)
    courier = models.ForeignKey(Profile, related_name='courier_orders', null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'orders'

    def __str__(self):
        return f'Order # {self.id}'

    def get_order_price(self):
        total_price = 0
        for item in self.orderitem_set.all():
            total_price += item.dish_price * item.dish_quantity
        return total_price


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, null=True, on_delete=models.SET_NULL)
    dish_price = models.DecimalField(max_digits=10, decimal_places=2)
    dish_name = models.CharField(max_length=250)
    dish_quantity = models.IntegerField(default=1)

    class Meta:
        db_table = 'order_items'

    def __str__(self):
        return f'Order # {self.id} - Dish {self.dish_name}'
