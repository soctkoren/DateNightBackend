from address.models import AddressField
from django.db import models

class Address(models.Model):
  address = AddressField(on_delete=models.CASCADE)
