# users/views.py

from django.shortcuts import render, redirect
from allauth.account.views import SignupView
from .forms import PetOwnerSignUpForm, PetSitterSignUpForm
from users.models import PetOwner, PetSitter

class PetOwnerSignUpView(SignupView):
    form_class = PetOwnerSignUpForm

    template_name = 'users/registration/pet_owner_signup.html'  # Create this template

    def form_valid(self, form):
        import pdb
        pdb.set_trace()
        response = super().form_valid(form)
        PetOwner.objects.create(user=self.user, contact_number=form.cleaned_data['contact_number'],zipcode=form.cleaned_data['zipcode'])
        return response

class PetSitterSignUpView(SignupView):
    form_class = PetSitterSignUpForm
    template_name = 'registration/pet_sitter_signup.html'  # Create this template

    def form_valid(self, form):
        response = super().form_valid(form)
        PetSitter.objects.create(
            user=self.user,
            certifications=form.cleaned_data['certifications'],
            email=form.cleaned_data['email'],
            address=form.cleaned_data['address'],
            zipcode=form.cleaned_data['zipcode']
        )
        return response
