from django.db import models

class Task(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    text = models.CharField(max_length=200)
    isDone = models.BooleanField(default=False)