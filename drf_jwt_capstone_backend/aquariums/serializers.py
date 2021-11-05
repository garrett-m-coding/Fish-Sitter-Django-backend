from rest_framework import serializers
from .models import Aquarium

class AquariumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aquarium
        fields = ['id', 'is_active', 'water_capacity', 'name', 'user_id']