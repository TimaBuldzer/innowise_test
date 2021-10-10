from django.urls import path

from apps.orders.api import views

urlpatterns = [
    path('orders/', views.OrderListCreateApiView.as_view()),
]
