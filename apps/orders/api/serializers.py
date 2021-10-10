from rest_framework import serializers
from apps.orders import models as orders_models


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = orders_models.OrderItem


class OrderSerializer(serializers.ModelSerializer):
    orderitem = OrderItemSerializer()

    class Meta:
        model = orders_models.Order
