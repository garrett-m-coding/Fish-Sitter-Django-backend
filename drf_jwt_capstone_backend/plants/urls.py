from django.urls import path
from plants import views

urlpatterns = [
    path('users/', views.aquarium_plants),
    path('details/<int:aquarium_id>', views.plants_details),
    ]