from rest_framework import serializers
from apps.orders import models as orders_models
from apps.restaurants import models as restaurant_models


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = orders_models.OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    order_item = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()
    destination_address = serializers.CharField(required=False, write_only=True)

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
        restaurant_ids = profile.cart.cartitem_set.distinct('dish').values_list('dish__restaurant', flat=True)

        for rest_id in restaurant_ids:
            order = self.create_order(profile, rest_id, validated_data)
            for cart_item in profile.cart.cartitem_set.filter(dish__restaurant_id=rest_id):
                self.create_order_item(order, cart_item)
        profile.cart.clear_cart()
        return order

    @staticmethod
    def create_order(profile, rest_id, data):
        restaurant = restaurant_models.Restaurant.objects.get(id=rest_id)
        return orders_models.Order.objects.create(
            profile=profile,
            restaurant=restaurant,
            source_address=restaurant.address,
            destination_address=data.get('destination_address') if data.get('destination_address') else profile.address
        )

    @staticmethod
    def create_order_item(order, cart_item):
        orders_models.OrderItem.objects.create(
            order=order,
            dish=cart_item.dish,
            dish_name=cart_item.dish.name,
            dish_price=cart_item.price,
            dish_quantity=cart_item.quantity
        )

    @staticmethod
    def get_order_item(obj: orders_models.Order):
        return OrderItemSerializer(obj.orderitem_set.all(), many=True).data

    @staticmethod
    def get_total_price(obj):
        return obj.get_order_price()

