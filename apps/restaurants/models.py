from django.db import models

from apps.users.models import Profile


class Restaurant(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'restaurants'

    def __str__(self):
        return f'{self.name} - {self.address}'


class Employee(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    class Meta:
        db_table = 'employees'

    def __str__(self):
        return f'{self.profile}'


class Dish(models.Model):
    image = models.ImageField(upload_to='restaurants/dishes/%Y/%m/%d', null=True, blank=True)
    name = models.CharField(max_length=250)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'dishes'

    def __str__(self):
        return f'{self.name} - {self.restaurant}'

    def get_price(self):
        if self.discount.discount_type == DiscountType.DISCOUNT:
            discounted = self.price * self.discount.percentage / 100
            return self.price - discounted
        return self.price


class DiscountType(models.TextChoices):
    DISCOUNT = 'discount', 'Discount'
    ONE_PLUS_ONE = 'one plus one', 'One plus one'


class Discount(models.Model):
    dish = models.OneToOneField(Dish, on_delete=models.CASCADE)
    percentage = models.IntegerField(default=0)
    discount_type = models.CharField(max_length=25, default=DiscountType.DISCOUNT, choices=DiscountType.choices)

    class Meta:
        db_table = 'discounts'

    def __str__(self):
        return f'{self.dish} - {self.discount_type}'
