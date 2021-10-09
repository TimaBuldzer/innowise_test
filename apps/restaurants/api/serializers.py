from rest_framework import serializers
from apps.restaurants import models as restaurant_models


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = restaurant_models.Dish
        fields = '__all__'
