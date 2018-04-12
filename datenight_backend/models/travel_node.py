from django.db import models

class TravelNode(models.Model):
    travel_method = models.TextField(max_length=None)
    estimated_travel_time = models.IntegerField
