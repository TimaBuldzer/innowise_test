from apps.orders import models as orders_models
from rest_framework.generics import ListCreateAPIView
from apps.orders.api import serializers as rest_serializers
from apps.users import models as users_models


class OrderListCreateApiView(ListCreateAPIView):
    serializer_class = rest_serializers.OrderSerializer

    def get_queryset(self):
        profile: users_models.Profile = self.request.user.profile
        if profile.role == users_models.ProfileRole.USER:
            return orders_models.Order.objects.filter(profile=profile)
        elif profile.role == users_models.ProfileRole.COURIER:
            return orders_models.Order.objects.filter(courier=profile)
        elif profile.role == users_models.ProfileRole.MANAGER:
            return orders_models.Order.objects.filter(restaurant=profile.employee.restaurant)
        return orders_models.Order.objects.none()
