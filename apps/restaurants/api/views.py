from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.restaurants.api import serializers as rest_serializers
from apps.restaurants import models as restaurant_models


class DishListCreateApiView(ListCreateAPIView):
    queryset = restaurant_models.Dish.objects.all()
    serializer_class = rest_serializers.DishSerializer
