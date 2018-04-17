from django.db import models
from .node import Node

class TravelNode(models.Model):
    travel_method = models.TextField(max_length=None)
    estimated_travel_time = models.IntegerField
    node = models.ForeignKey(Node, default=1, on_delete=models.CASCADE)
