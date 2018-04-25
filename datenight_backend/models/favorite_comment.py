from django.db import models
from django.contrib.auth.models import User
from .comment import Comment

class FavoriteComment(models.Model):
    favorite_comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
