from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Redflag(models.Model):
    title = models.CharField(max_length=100)
    comment = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=200, default='pending')
    image = models.TextField()
    video = models.TextField()
    createdby = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, to_field='username')
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.title