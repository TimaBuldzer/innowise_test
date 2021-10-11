from django.contrib.auth.models import User
from django.db import models


class ProfileRole(models.TextChoices):
    USER = 'user', 'User'
    MANAGER = 'manager', 'Manager'
    COURIER = 'courier', 'Courier'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, default=ProfileRole.USER, choices=ProfileRole.choices)
    address = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        db_table = 'profiles'

    def __str__(self):
        return f'{self.user} {self.role}'


class Cart(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    class Meta:
        db_table = 'carts'

    def __str__(self):
        return f'{self.profile} cart'

    def clear_cart(self):
        self.cartitem_set.all().delete()


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    dish = models.ForeignKey('restaurants.Dish', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)

    class Meta:
        db_table = 'cart_items'

    def __str__(self):
        return f'{self.cart} : {self.dish}'


class Report(models.Model):
    reported_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'reports'

    def __str__(self):
        return f'{self.reported_profile} - {self.order} - {self.created_dt}'
