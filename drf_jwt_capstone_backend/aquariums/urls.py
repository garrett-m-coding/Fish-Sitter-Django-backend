from django.urls import path
from aquariums import views

urlpatterns = [
    path('all/', views.get_all_aquariums),
    path('users/', views.user_aquariums),
    path('details/<int:pk>', views.aquarium_details)
    ]