from django.db import models
from django.contrib.auth.models import User

class LostFoundID(models.Model):
    STATUS_CHOICES = (
        ('lost', 'Lost'),
        ('found', 'Found'),
    )

    id_number = models.CharField(max_length=20, unique=True)
    status = models.CharField(max_length=5, choices=STATUS_CHOICES)
    location = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date_reported = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_number} - {self.status}"


