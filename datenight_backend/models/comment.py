from django.db import models
from django.contrib.auth.models import User
from .node import Node

class Comment(models.Model):
    content = models.TextField(max_length=280)
    is_hidden = models.BooleanField(default=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    node = models.ForeignKey(Node, default=1, on_delete=models.CASCADE)
