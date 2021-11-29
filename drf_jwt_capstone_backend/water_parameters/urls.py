from django.urls import path
from water_parameters import views

urlpatterns = [
    path('users/', views.aquarium_water_parameters),
    path('details/<int:aquarium_id>', views.water_parameters_details),
    ]