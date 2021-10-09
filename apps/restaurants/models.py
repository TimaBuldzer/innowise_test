from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    email = models.EmailField()

    class Meta:
        db_table = 'restaurants'

    def __str__(self):
        return f'{self.name} - {self.address}'

# class Dish(models.Model):
#     name = models.CharField(max_length=250)
#     restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
