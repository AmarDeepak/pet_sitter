# users/forms.py

from django import forms
from allauth.account.forms import SignupForm
from .models import PetOwner, PetSitter, CustomUser, Pet

class PetOwnerSignUpForm(SignupForm):
    first_name = forms.CharField(label=("First Name"),max_length=15, required=True,
                                     widget=forms.TextInput(attrs={
                                         "type": "text",
                                         "placeholder": ("First Name"),
                                         "autocomplete": "first_name",
                                     })
                                     )
    last_name = forms.CharField(label=("Last Name"), max_length=15, required=True,
                                 widget=forms.TextInput(attrs={
                                     "type": "text",
                                     "placeholder": ("Last Name"),
                                     "autocomplete": "last_name",
                                 })
                                 )
    contact_number = forms.CharField(label=("Contact Number"),max_length=15, required=False,
                                     widget=forms.TextInput(attrs={
                                         "type": "text",
                                         "placeholder": ("Contact Number"),
                                         "autocomplete": "contact",
                                     })
                                     )
    zipcode = forms.CharField(max_length=15, required=False,
                              widget=forms.TextInput(attrs={
                                  "type": "text",
                                  "placeholder": ("zipcode"),
                                  "autocomplete": "zipcode",
                              })
                              )

    class Meta:
        model = PetOwner

class PetSitterSignUpForm(SignupForm):
    certifications = forms.CharField(widget=forms.Textarea, required=False)
    email = forms.EmailField()
    address = forms.CharField(max_length=350, required=False)
    zipcode = forms.CharField(max_length=15, required=False)

    class Meta:
        model = PetSitter
        fields = ('certifications', 'email', 'address', 'zipcode')

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'species', 'breed', 'age', 'weight', 'photo']

