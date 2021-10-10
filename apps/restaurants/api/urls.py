from django.urls import path

from apps.restaurants.api import views

urlpatterns = [
    path('dishes/', views.DishListCreateApiView.as_view()),
    path('dishes/<int:pk>/', views.DishRetrieveUpdateDeleteView.as_view()),

    path('restaurants/', views.RestaurantListCreateApiView.as_view()),
    path('restaurants/<int:pk>/', views.RestaurantRetrieveUpdateView.as_view()),

]
