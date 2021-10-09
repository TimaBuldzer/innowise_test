from django.db import models

from apps.users.models import Profile


class Restaurant(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    email = models.EmailField()

    class Meta:
        db_table = 'restaurants'

    def __str__(self):
        return f'{self.name} - {self.address}'


class Employee(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)

    class Meta:
        db_table = 'employees'

    def __str__(self):
        return f'{self.user}'


class Dish(models.Model):
    name = models.CharField(max_length=250)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    class Meta:
        db_table = 'dishes'

    def __str__(self):
        return f'{self.name} - {self.restaurant}'
