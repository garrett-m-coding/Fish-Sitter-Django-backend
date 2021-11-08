from rest_framework import serializers
from .models import Food

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'food_type', 'fed_food', 'date_fed', 'before_noon', 'after_noon', 'aquarium']