from rest_framework import serializers
from apps.restaurants import models as restaurant_models


class DishSerializer(serializers.ModelSerializer):
    discount_type = serializers.CharField(required=False, write_only=True)
    discount_percentage = serializers.FloatField(required=False, write_only=True)

    class Meta:
        model = restaurant_models.Dish
        fields = '__all__'

    def create(self, validated_data):
        instance = super(DishSerializer, self).create(validated_data)
        if validated_data.get('discount_type'):
            restaurant_models.Discount.objects.create(
                dish=instance,
                discount_type=restaurant_models.DiscountType.DISCOUNT,
                discount_percentage=validated_data.get('discount_percentage')
            )
        return instance


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = restaurant_models.Restaurant
        fields = '__all__'
