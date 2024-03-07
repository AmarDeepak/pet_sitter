# forms.py
from django import forms
from .models import Appointment
from users.models import PetSitter

class AppointmentForm(forms.ModelForm):
    # Add a new field for the selected pet sitter
    selected_pet_sitter = forms.ModelChoiceField(queryset=PetSitter.objects.all(), label="Select Pet Sitter")

    class Meta:
        model = Appointment
        fields = ['first_name', 'last_name', 'email','phone','appointment_date', 'sitter','user', 'selected_pet_sitter']
