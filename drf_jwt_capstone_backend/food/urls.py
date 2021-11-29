from django.urls import path
from food import views

urlpatterns = [
    path('users/', views.aquarium_food),
    path('details/<int:aquarium_id>', views.food_details),
    ]