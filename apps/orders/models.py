from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

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


class Order(MPTTModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, null=True, on_delete=models.CASCADE)
    parent = TreeForeignKey('self', on_delete=models.CASCADE)
    status = models.CharField(max_length=25, default=OrderStatus.NEW, choices=OrderStatus.choices)

    class Meta:
        db_table = 'orders'

    def __str__(self):
        return f'Order # {self.id}'

    def get_price(self):
        if self.parent:
            total_price = 0
            for order in self.order_set.all():
                total_price += self.get_order_price(order)
            return total_price
        else:
            return self.get_order_price(self)

    @staticmethod
    def get_order_price(obj):
        return obj.orderitem.dish_price * obj.orderitem.dish_quantity


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
