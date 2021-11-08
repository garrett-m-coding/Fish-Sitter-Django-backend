from rest_framework import serializers
from .models import Fish

class FishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fish
        fields = ['id', 'fish_type', 'is_alive', 'number_of_fish', 'aquarium']