from rest_framework import serializers
from apps.orders import models as orders_models


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = orders_models.OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    order_item = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = orders_models.Order
        exclude = ['profile']
        extra_kwargs = {
            'status': {'read_only': True},
            'restaurant': {'read_only': True},
            'courier': {'read_only': True}
        }

    def create(self, validated_data):
        profile = self.context.get('request').user.profile
        order = None
        for cart_item in profile.cart.cartitem_set.all():
            order = orders_models.Order.objects.create(
                profile=profile,
                restaurant=cart_item.dish.restaurant
            )
            orders_models.OrderItem.objects.create(
                order=order,
                dish=cart_item.dish,
                dish_name=cart_item.dish.name,
                dish_price=cart_item.dish.price,
                dish_quantity=cart_item.quantity
            )

        return order

    def get_order_item(self, obj: orders_models.Order):
        return OrderItemSerializer(obj.orderitem).data

    def get_total_price(self, obj):
        return obj.get_order_price()
