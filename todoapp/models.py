from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100)
    priority = models.IntegerField()
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
