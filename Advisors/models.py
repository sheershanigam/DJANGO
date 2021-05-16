# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Advisors(models.Model):
    name = models.CharField(max_length=200)
    photo_url = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class AdvisorAppointments(models.Model):
    bookingTime = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    advisor = models.ForeignKey(Advisors, on_delete=models.CASCADE, null=False)
