# dashboard/models.py

from django.db import models
from users.models import CustomUser, PetSitter, PetOwner

class Dashboard(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    pet_owner_bookings = models.PositiveIntegerField(default=0)
    pet_owner_expenditure = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    pet_sitter_bookings = models.PositiveIntegerField(default=0)
    pet_sitter_earnings = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"Dashboard for {self.user.username}"


class Appointment(models.Model):
    user = models.ForeignKey(PetOwner, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    request = models.TextField(blank=True)
    sent_date = models.DateField(auto_now_add=True)
    appointment_date = models.DateField(auto_now_add=False, null=True, blank=True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateField(auto_now_add=False, null=True, blank=True)
    sitter = models.ForeignKey(PetSitter, on_delete=models.PROTECT)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ["-sent_date"]
