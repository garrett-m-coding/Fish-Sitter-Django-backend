from django.urls import path
from aquariums import views

urlpatterns = [
    path('all/', views.get_all_aquariums),
    path('', views.user_aquariums)
    ]