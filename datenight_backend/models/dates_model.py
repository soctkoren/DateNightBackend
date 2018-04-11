from django.db import models

class Dates(models.Model):
    date_description = models.CharField(max_length=200)
    is_public = models.BooleanField(default=False)
    is_created = models.BooleanField(default=False)
