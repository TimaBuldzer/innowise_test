from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveUpdateAPIView

from apps.restaurants.api import serializers as rest_serializers
from apps.restaurants import models as restaurant_models


class DishListCreateApiView(ListCreateAPIView):
    queryset = restaurant_models.Dish.objects.filter(is_active=True)
    serializer_class = rest_serializers.DishSerializer


class DishRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = restaurant_models.Dish
    serializer_class = rest_serializers.DishSerializer


class RestaurantListCreateApiView(ListAPIView):
    queryset = restaurant_models.Restaurant.objects.filter(is_active=True)
    serializer_class = rest_serializers.RestaurantSerializer


class RestaurantRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = restaurant_models.Restaurant
    serializer_class = rest_serializers.RestaurantSerializer
