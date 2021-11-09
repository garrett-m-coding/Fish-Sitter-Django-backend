from django.db import models
from django.contrib.auth import get_user_model
from aquariums.models import Aquarium
User = get_user_model()

# Create your models here.


class Water_Parameter(models.Model):
    aquarium = models.ForeignKey(Aquarium, on_delete=models.CASCADE)
    general_hardness_ppm = models.IntegerField()
    carbonate_hardness_ppm = models.IntegerField()
    power_of_hydrogen = models.DecimalField(max_digits = 2,decimal_places=1)
    nitrites_ppm = models.IntegerField()
    nitrates_ppm = models.IntegerField()
    temperature_fahrenheit = models.IntegerField()
    water_changed = models.BooleanField()
    gallons_water_added = models.IntegerField()
    date_measured = models.DateField()
    before_noon = models.BooleanField()
    after_noon = models.BooleanField()