from django.db import models
from .node import Node
from .image import Image

class DestinationNode(models.Model):
    description = models.CharField(max_length=200)
    node = models.ForeignKey(Node, default=1, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, null=True, on_delete=models.CASCADE)
