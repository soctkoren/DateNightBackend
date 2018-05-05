from address.models import AddressField
from django.db import models

class Address(models.Model):
  address = AddressField()
