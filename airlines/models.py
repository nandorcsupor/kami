# airlines/models.py
from django.db import models
import math

class Airplane(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    passengers = models.PositiveIntegerField(default=0)

    def fuel_tank_capacity(self):
        return 200 * self.id

    def fuel_consumption_per_minute(self):
        return math.log(self.id) * 0.80
