from django.db import models

class Reminders(models.Model):
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()