from django.db import models
from django.contrib.auth import get_user_model
from aquariums.models import Aquarium
User = get_user_model()

# Create your models here.
class Plant(models.Model):
    aquarium = models.ForeignKey(Aquarium, on_delete=models.CASCADE)
    plant_type = models.CharField(max_length=100)
    plant_trimmed = models.BooleanField()
    date_trimmed = models.DateField()