# users/forms.py


from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from djchoices import ChoiceItem, DjangoChoices


class CustomUser(AbstractUser):
    class UserType(DjangoChoices):
        petowner = ChoiceItem("petowner")
        petsitter = ChoiceItem("petsitter")
    # Additional fields for your custom user model (if needed)
    # For example, you might want to include a profile picture.
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    user_type = models.TextField(choices=UserType.choices,default=UserType.petowner, null=True, blank=True)

    def __str__(self):
        return self.username

class PetOwner(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Additional fields specific to pet owners
    # For example, you might include contact information.
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    zipcode = models.CharField(max_length=15, blank=True, null=True)
    user_type = models.CharField(max_length=15, default="pet-owner", null=True, blank=True)
    def __str__(self):
        return f"Pet Owner: {self.user.username}"

@receiver(user_signed_up)
def user_signed_up_handler(request, user, **kwargs):
    # Additional actions to perform when a user signs up (e.g., send welcome email)
    pass

class PetSitter(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Additional fields specific to pet sitters
    # For example, you might include certifications or experience.
    certifications = models.TextField(blank=True, null=True)
    email = models.EmailField()
    address = models.CharField(max_length=350, blank=True, null=True)
    zipcode = models.CharField(max_length=15, blank=True, null=True)
    user_type = models.CharField(max_length=15, default="pet-sitter", null=True, blank=True)

    def __str__(self):
        return f"Pet Sitter: {self.user.username}"