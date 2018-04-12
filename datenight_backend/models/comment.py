from django.db import models

class Comment(models.Model):
    content = models.TextField(max_length=280)
    is_hidden = models.BooleanField(default=True)
