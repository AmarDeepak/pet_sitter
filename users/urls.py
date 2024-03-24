# users/urls.py

from django.urls import path
from .views import PetOwnerSignUpView, PetSitterSignUpView, create_pet_api, pet_list_api

urlpatterns = [
    path('accounts/signup/pet-owner/', PetOwnerSignUpView.as_view(), name='pet_owner_signup'),
    path('accounts/signup/pet-sitter/', PetSitterSignUpView.as_view(), name='pet_sitter_signup'),
    path('api/pet/create/', create_pet_api, name='create_pet_api'),
    path('api/pet/list/', pet_list_api, name='pet_list_api'),
]
