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
