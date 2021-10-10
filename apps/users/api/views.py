from apps.users import models as users_models
from apps.users.api import serializers as users_serializers
from rest_framework.generics import RetrieveAPIView, CreateAPIView


class CartRetrieveApiView(RetrieveAPIView):
    serializer_class = users_serializers.CartSerializer

    def get_object(self):
        return self.request.user.profile.cart


class CartItemCreateApiView(CreateAPIView):
    queryset = users_models.CartItem
    serializer_class = users_serializers.CartItemSerializer
