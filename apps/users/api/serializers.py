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
    dish = serializers.SerializerMethodField()
    dish_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = users_models.CartItem
        exclude = ['cart']

    def create(self, validated_data):
        cart = self.context.get('request').user.profile.cart
        obj = users_models.CartItem.objects.create(
            cart=cart,
            dish_id=validated_data.get('dish_id')
        )
        return obj

    def get_dish(self, obj):
        return DishSerializer(obj.dish, read_only=True).data
