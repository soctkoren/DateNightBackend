from django.db import models
from .date import Date
from .tag import Tag

class DateTag(models.Model):
    date = models.ForeignKey(Date, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
