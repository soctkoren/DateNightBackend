from django.db import models
from .node import Node
from .image import Image
from .address import Address

class DestinationNode(models.Model):
    description = models.CharField(max_length=200)
    node = models.ForeignKey(Node, default=1, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, null=True, on_delete=models.CASCADE)
    destination_address = models.ForeignKey(Address, null=True, on_delete=models.CASCADE)

    def create_payload(self):
        payload = {}
        payload['destination_id'] = self.id
        payload['description'] = self.description
        payload['image'] = self.image
        #TODO think about a better structure for sending back address
        payload['destination_address'] = self.destination_address.address.raw
        return payload
