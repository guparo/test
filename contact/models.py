from django.db import models
import time

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    creation_date = time.asctime( time.localtime(time.time()) )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
