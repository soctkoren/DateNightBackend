from django.db import models
from django.contrib.auth.models import User
from .date import Date

class FavoriteDate(models.Model):
    favorite_date = models.ForeignKey(Date, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
