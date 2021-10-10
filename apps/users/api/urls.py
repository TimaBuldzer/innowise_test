from django.urls import path
from . import views

urlpatterns = [
    path('report/', views.ReportListCreateApiView.as_view()),

    path('cart/add-item/', views.CartItemCreateApiView.as_view()),
    path('cart/item/<int:pk>/', views.CartItemRetrieveUpdateDestroyApiView.as_view()),
    path('cart/', views.CartRetrieveApiView.as_view()),
]
