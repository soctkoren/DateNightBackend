from django.db import models
from .image import Image

class Date(models.Model):
    date_description = models.CharField(max_length=200)
    is_public = models.BooleanField(default=False)
    is_created = models.BooleanField(default=False)
    image = models.ForeignKey(Image, null=True, on_delete=models.CASCADE)
