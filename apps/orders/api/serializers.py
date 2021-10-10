from rest_framework import serializers
from apps.orders import models as orders_models
from apps.restaurants import models as restaurants_models
from apps.restaurants.api import serializers as restaurant_serializers


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = orders_models.OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = orders_models.Order
        fields = '__all__'
        extra_kwargs = {
            'status': {'read_only': True},
            'parent': {'read_only': True},
            'profile': {'read_only': True},
            'restaurant': {'read_only': True},
        }

    def create(self, validated_data):
        user = self.context.get('request').user

        parent_order = orders_models.Order.objects.create(
            profile=user.profile,
        )
        for d in validated_data.get('dish_ids'):
            dish = restaurants_models.Dish.objects.get(id=d.get('id'))
            order = orders_models.Order.objects.create(
                parent=parent_order,
                profile=user.profile,
                restaurant=dish.restaurant
            )
            orders_models.OrderItem.objects.create(
                order=order,
                dish=dish,
                dish_name=dish.name,
                dish_price=dish.price,
                dish_quantity=d.get('quantity')
            )
