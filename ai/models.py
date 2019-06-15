from django.db import models
from django.utils import timezone

# Create your models here.
class TestData(models.Model):
    pred = models.IntegerField()

    def __str__(self):
        return self.pred
