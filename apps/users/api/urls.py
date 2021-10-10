from django.urls import path
from . import views

urlpatterns = [
    path('cart/add-item/', views.CartItemCreateApiView.as_view()),
    path('cart/', views.CartRetrieveApiView.as_view()),
]
