from apps.restaurants.api.serializers import DishSerializer
from apps.users import models as users_models
from rest_framework import serializers


class CartSerializer(serializers.ModelSerializer):
    cart_items = serializers.SerializerMethodField()

    class Meta:
        model = users_models.Cart
        exclude = ['profile']

    def get_cart_items(self, obj: users_models.Cart):
        queryset = obj.cartitem_set.all()
        data = CartItemSerializer(queryset, many=True).data
        return data


class CartItemSerializer(serializers.ModelSerializer):
    dish = DishSerializer()

    class Meta:
        model = users_models.CartItem
        exclude = ['cart']
