from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
import time



class Passenger(models.Model):
    name = models.CharField(max_length=150)
    image  = models.FileField()
    survived = models.BooleanField()
    age = models.DecimalField(max_digits=4, decimal_places=2) 
    sexo = models.CharField(max_length=10)
    text = models.TextField()

    ticket_class = models.PositiveSmallIntegerField(default=1,
        validators=[
            MaxValueValidator(3),
            MinValueValidator(1)
        ])
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('passenger_edit', kwargs={'pk': self.pk})


