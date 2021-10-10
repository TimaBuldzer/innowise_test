from apps.orders import models as orders_models
from rest_framework.generics import ListCreateAPIView
from apps.orders.api import serializers as rest_serializers


class OrderListCreateApiView(ListCreateAPIView):
    serializer_class = rest_serializers.OrderSerializer
    queryset = orders_models.Order.objects.all()  # TODO add filter_queryset and filter by restaurant id or all
