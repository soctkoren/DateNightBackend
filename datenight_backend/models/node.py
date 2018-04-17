from django.db import models
from .date import Date

class Node(models.Model):
    order_number = models.SmallIntegerField()
    is_hidden = models.BooleanField(default=True)
    date = models.ForeignKey(Date, null=True, on_delete=models.CASCADE)
