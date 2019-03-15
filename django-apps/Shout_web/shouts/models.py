import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Shout(models.Model):
    shout_text = models.CharField(max_length=200)
    shout_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.shout_text
