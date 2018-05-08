from django.db import models
from .date import Date

class Node(models.Model):
    order_number = models.SmallIntegerField()
    is_hidden = models.BooleanField(default=True)
    date = models.ForeignKey(Date, null=True, on_delete=models.CASCADE)

    def create_payload(self):
        payload = {}
        payload['node_id'] = self.id
        payload['order_number'] = self.order_number
        payload['is_hidden'] = self.is_hidden
        return payload
