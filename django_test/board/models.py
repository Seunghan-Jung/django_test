from django.conf import settings
from django.db import models


class Board(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
