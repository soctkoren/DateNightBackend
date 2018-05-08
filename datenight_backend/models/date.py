from django.db import models
from .image import Image
from datenight_backend.workers.serializer import serialize_for_json

class Date(models.Model):
    date_name = models.CharField(max_length=200, default='Untitled')
    date_description = models.CharField(max_length=200, default='')
    is_public = models.BooleanField(default=False)
    is_created = models.BooleanField(default=False)
    image = models.ForeignKey(Image, null=True, on_delete=models.CASCADE)

    def create_payload(self):
        payload = {}
        payload['date_id'] = self.id
        payload['date_description'] = self.date_description
        payload['is_public'] = self.is_public
        payload['is_created'] = self.is_created
        payload['image'] = serialize_for_json(self.image)
        return payload
