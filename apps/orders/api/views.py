import datetime

from django.db.models import Q
from django.http import Http404
from rest_framework.response import Response

from apps.orders import models as orders_models
from rest_framework.generics import ListCreateAPIView, GenericAPIView
from apps.orders.api import serializers as rest_serializers
from apps.users import models as users_models


class OrderListCreateApiView(ListCreateAPIView):
    serializer_class = rest_serializers.OrderSerializer

    def get_queryset(self):
        profile: users_models.Profile = self.request.user.profile
        if profile.role == users_models.ProfileRole.USER:
            return orders_models.Order.objects.filter(profile=profile)
        elif profile.role == users_models.ProfileRole.COURIER:
            return orders_models.Order.objects.filter(Q(courier=profile) | Q(status=orders_models.OrderStatus.READY))
        elif profile.role == users_models.ProfileRole.MANAGER:
            return orders_models.Order.objects.filter(restaurant=profile.employee.restaurant)
        return orders_models.Order.objects.none()


class AssignCourierToOrderApiView(GenericAPIView):
    def post(self, request, *args, **kwargs):
        order = orders_models.Order.objects.get(id=kwargs.get('pk'))
        self.validate_request(order)

        order.courier = request.user.profile
        order.status = orders_models.OrderStatus.ON_THE_WAY
        order.save(update_fields=['courier', 'status'])

        return Response(status=200)

    def validate_request(self, order):
        if self.request.user.profile.role != users_models.ProfileRole.COURIER:
            raise Http404
        if order.status != orders_models.OrderStatus.READY:
            raise Http404


class ChangeOrderStatusToDeliveredApiView(GenericAPIView):
    def post(self, request, *args, **kwargs):
        order = orders_models.Order.objects.get(id=kwargs.get('pk'))
        self.validate_request(order)

        order.status = orders_models.OrderStatus.DELIVERED
        order.delivered_dt = datetime.datetime.now()
        order.save(update_fields=['status'])
        return Response(status=200)

    def validate_request(self, order):
        if self.request.user.profile.role != users_models.ProfileRole.COURIER:
            raise Http404
        if order.status != orders_models.OrderStatus.ON_THE_WAY:
            raise Http404

