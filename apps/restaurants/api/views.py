from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.restaurants.api import serializers as rest_serializers
from apps.restaurants import models as restaurant_models


class DishListCreateApiView(ListCreateAPIView):
    queryset = restaurant_models.Dish.objects.all()
    serializer_class = rest_serializers.DishSerializer


class DishRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = restaurant_models.Dish
    serializer_class = rest_serializers.DishSerializer
