from django.urls import path

from apps.restaurants.api.views import DishListCreateApiView

urlpatterns = [
    path('dishes/', DishListCreateApiView.as_view())
]
