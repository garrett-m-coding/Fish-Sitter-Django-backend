from django.urls import path
from food import views

urlpatterns = [
    path('users/', views.aquarium_food),
    path('details/<int:fk>', views.food_details),
    ]