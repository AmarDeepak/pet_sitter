"""pet_sitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from dashboard.views import petowner, petsitter, HomeTemplateView
from users.views import PetOwnerSignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/signup/', PetOwnerSignUpView.as_view()),
    path('petowner/', petowner, name='petowner'),
    path('',HomeTemplateView.as_view(), name='home'),

    path("", include("dashboard.urls"))
]
