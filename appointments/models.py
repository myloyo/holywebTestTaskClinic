from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    full_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.full_name} ({self.specialization})"

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.user} — {self.doctor} — {self.date} {self.time}"
