# users/views.py
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from allauth.account.views import SignupView
from users.forms import PetOwnerSignUpForm, PetSitterSignUpForm, PetForm
from users.models import PetOwner, PetSitter, CustomUser, Pet
from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required

class PetOwnerSignUpView(SignupView):
    form_class = PetOwnerSignUpForm
    template_name = 'users/registration/pet_owner_signup.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        response = super().form_valid(form)

        # Add your custom logic to create the PetOwner object
        PetOwner.objects.create(
            user=self.user,
            contact_number=form.cleaned_data['contact_number'],
            zipcode=form.cleaned_data['zipcode'],
        )
        self.user.user_type = CustomUser.UserType.petowner
        self.user.save()
        return response

    def form_invalid(self, form):
        print("Form is invalid. Errors:", form.errors)
        return self.render_to_response(self.get_context_data(form=form))
        # return self.render_to_response(self.get_context_data(form=form))
    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     if form.errors:
    #         print(form.errors)
    #     PetOwner.objects.create(user=self.user, contact_number=form.cleaned_data['contact_number'],zipcode=form.cleaned_data['zipcode'])
    #     return response

class PetSitterSignUpView(SignupView):
    form_class = PetSitterSignUpForm
    template_name = 'users/registration/pet_sitter_signup.html'  # Create this template

    def form_valid(self, form):
        response = super().form_valid(form)
        PetSitter.objects.create(
            user=self.user,
            certifications=form.cleaned_data['certifications'],
            email=form.cleaned_data['email'],
            address=form.cleaned_data['address'],
            zipcode=form.cleaned_data['zipcode']
        )
        self.user.user_type = CustomUser.UserType.petsitter
        self.user.save()
        return response

# @login_required
def create_pet_api(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.owner = request.user
            pet.save()
            return JsonResponse({'success': True, 'message': 'Pet created successfully'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)

def pet_list_api(request):
    pets = Pet.objects.filter(owner=request.user)
    data = [{'name': pet.name, 'species': pet.species} for pet in pets]
    return JsonResponse(data, safe=False)
