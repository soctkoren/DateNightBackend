from address.models import AddressField
from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
  address = AddressField(on_delete=models.CASCADE)
  user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
