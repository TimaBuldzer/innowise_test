from apps.users import models as users_models
from apps.users.api import serializers as users_serializers
from rest_framework.generics import RetrieveAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView


class CartRetrieveApiView(RetrieveAPIView):
    serializer_class = users_serializers.CartSerializer

    def get_object(self):
        return self.request.user.profile.cart


class CartItemCreateApiView(CreateAPIView):
    queryset = users_models.CartItem
    serializer_class = users_serializers.CartItemSerializer


class CartItemRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = users_models.CartItem
    serializer_class = users_serializers.CartItemSerializer
    http_method_names = ['get', 'put', 'delete']
