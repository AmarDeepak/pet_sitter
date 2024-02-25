# users/urls.py

from django.urls import path
from .views import PetOwnerSignUpView, PetSitterSignUpView

urlpatterns = [
    path('accounts/signup/pet-owner/', PetOwnerSignUpView.as_view(), name='pet_owner_signup'),
    path('accounts/signup/pet-sitter/', PetSitterSignUpView.as_view(), name='pet_sitter_signup'),
]
