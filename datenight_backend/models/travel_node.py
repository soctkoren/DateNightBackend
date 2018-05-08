from django.db import models
from .node import Node
from .address import Address

class TravelNode(models.Model):
    travel_method = models.TextField(max_length=None)
    estimated_travel_time = models.IntegerField
    node = models.ForeignKey(Node, default=1, on_delete=models.CASCADE)
    starting_address = models.ForeignKey(Address, null=True, on_delete=models.CASCADE, related_name='start')
    destination_address = models.ForeignKey(Address, null=True, on_delete=models.CASCADE, related_name='end')
