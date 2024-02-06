from django.shortcuts import render

# Create your views here.

def petowner(request):
    return render(request, 'dashboard/pet_owner_dashboard.html')

def petsitter(request):
    return render(request, 'dashboard/pet_sitter_dashboard.html')
