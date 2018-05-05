from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    img_url = models.ImageField()
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
