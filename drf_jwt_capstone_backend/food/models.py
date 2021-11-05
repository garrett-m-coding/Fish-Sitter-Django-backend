from django.db import models
from django.contrib.auth import get_user_model
from aquariums.models import Aquarium
User = get_user_model()

# Create your models here.
class Food(models.Model):
    aquarium = models.ForeignKey(Aquarium, on_delete=models.CASCADE)
    food_type = models.CharField(max_length=100)
    fed_food = models.BooleanField()
    date_fed = models.DateField()
    before_noon = models.BooleanField()
    after_noon = models.BooleanField()