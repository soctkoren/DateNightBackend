from django.db import models

class DestinationNode(models.Model):
    description = models.CharField(max_length=200)
