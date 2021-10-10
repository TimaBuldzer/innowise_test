import datetime
import time

from django.http import Http404

from apps.restaurants.api.serializers import DishSerializer
from apps.users import models as users_models
from rest_framework import serializers

from conf.settings.constants import REPORT_EXPIRE_TIME
import pytz

class CartSerializer(serializers.ModelSerializer):
    cart_items = serializers.SerializerMethodField()

    class Meta:
        model = users_models.Cart
        exclude = ['profile']

    def get_cart_items(self, obj: users_models.Cart):
        queryset = obj.cartitem_set.all()
        data = CartItemSerializer(queryset, many=True).data
        return data


class CartItemSerializer(serializers.ModelSerializer):
    dish = serializers.SerializerMethodField()
    dish_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = users_models.CartItem
        exclude = ['cart']

    def create(self, validated_data):
        cart = self.context.get('request').user.profile.cart
        obj = users_models.CartItem.objects.create(
            cart=cart,
            dish_id=validated_data.get('dish_id')
        )
        return obj

    def get_dish(self, obj):
        return DishSerializer(obj.dish, read_only=True).data


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = users_models.Report
        fields = '__all__'
        extra_kwargs = {
            'reported_profile': {'read_only': True}
        }
        depth = 1

    def create(self, validated_data):
        order = validated_data.get('order')
        order_date = time.mktime(order.delivered_dt.astimezone(pytz.timezone('Europe/Minsk')).timetuple())
        mins = (datetime.datetime.now().timestamp() - order_date) / 60
        if mins > REPORT_EXPIRE_TIME:
            raise Http404
        report = users_models.Report.objects.create(
            order=order,
            reported_profile=order.courier
        )
        return report
