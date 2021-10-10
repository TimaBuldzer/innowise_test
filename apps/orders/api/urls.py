from django.urls import path

from apps.orders.api import views

urlpatterns = [
    path('orders/<int:pk>/assign-courier/', views.AssignCourierToOrderApiView.as_view()),
    path('orders/<int:pk>/order-delivered/', views.ChangeOrderStatusToDeliveredApiView.as_view()),
    path('orders/', views.OrderListCreateApiView.as_view()),
]
