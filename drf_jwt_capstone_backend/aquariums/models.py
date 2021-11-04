from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Aquarium(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(True)
    water_capacity = models.IntegerField()