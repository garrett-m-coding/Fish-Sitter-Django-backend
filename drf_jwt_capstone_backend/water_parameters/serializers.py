from rest_framework import serializers
from .models import Water_Parameter


class Water_ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Water_Parameter
        fields = ['id', 'general_hardness_ppm', 'carbonate_hardness_ppm', 'power_of_hydrogen',
                  'nitrites_ppm', 'nitrates_ppm', 'temperature_fahrenheit', 'water_changed',
                  'gallons_water_added', 'date_measured', 'before_noon', 'after_noon', 'aquarium']
