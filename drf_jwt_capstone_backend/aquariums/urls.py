from django.urls import path
from aquariums import views

urlpatterns = [
    path('all/', views.get_all_aquariums),
    path('all/relations/', views.get_all_aquarium_relations),
    path('users/', views.user_aquariums),
    path('details/<int:pk>', views.aquarium_details)
    ]