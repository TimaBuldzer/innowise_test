from django.contrib import admin

from apps.users.models import Profile, Cart,  CartItem


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    pass