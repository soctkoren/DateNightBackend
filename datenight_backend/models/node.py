from django.db import models

class Node(models.Model):
    order_number = models.SmallIntegerField()
    is_hidden = models.BooleanField(default=True)
