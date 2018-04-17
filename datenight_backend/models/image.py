from django.db import models
from django.contrib.auth import User

class Image(models.Model):
    img_url = models.ImageField(upload_to='imgs/')
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
