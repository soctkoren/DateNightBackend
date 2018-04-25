from django.db import models
from django.contrib.auth.models import User
from .node import Node

class FavoriteNode(models.Model):
    favorite_node = models.ForeignKey(Node, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
