from django.urls import path
from fish import views

urlpatterns = [
    # path('all/', views.get_all_fish),
    path('users/', views.aquarium_fish),
    path('details/<int:aquarium_id>', views.fish_details),
    ]