from django.db import models
from django.contrib.auth import get_user_model
from aquariums.models import Aquarium
User = get_user_model()

# Create your models here.
class Fish(models.Model):
    aquarium = models.ForeignKey(Aquarium, on_delete=models.CASCADE)
    fish_type = models.CharField(max_length=100)
    is_alive = models.BooleanField()
    number_of_fish = models.IntegerField()