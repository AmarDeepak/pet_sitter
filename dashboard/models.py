# dashboard/models.py

from django.db import models
from users.models import CustomUser

class Dashboard(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    pet_owner_bookings = models.PositiveIntegerField(default=0)
    pet_owner_expenditure = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    pet_sitter_bookings = models.PositiveIntegerField(default=0)
    pet_sitter_earnings = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"Dashboard for {self.user.username}"
