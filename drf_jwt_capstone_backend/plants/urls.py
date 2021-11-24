from django.urls import path
from plants import views

urlpatterns = [
    path('users/', views.aquarium_plants),
    path('details/<int:fk>', views.plants_details),
    ]