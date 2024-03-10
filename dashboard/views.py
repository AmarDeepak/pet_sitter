from django.shortcuts import render,redirect,reverse

from .forms import AppointmentForm
from .models import Appointment
from django.http.response import HttpResponseRedirect
from django.http import HttpResponse
from django.views.generic.base import TemplateView, View
from django.core.mail import EmailMessage, message
from django.conf import settings
from django.contrib import messages
from django.views.generic import ListView
import datetime
from django.template.loader import render_to_string, get_template
from users.models import PetOwner, PetSitter, CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone

from django.template import Context
from django.urls import reverse
# Create your views here.

def petowner(request):
    #Need to validate the user.
    return render(request, 'dashboard.html')

def petsitter(request):
    return render(request, 'dashboard/pet_sitter_dashboard.html')


class HomeTemplateView(TemplateView):
    template_name = "dashboard.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pet_sitters"] = PetSitter.objects.all()
        return context
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, 'dashboard.html', context)
class AppointmentTemplateView(TemplateView):
    template_name = "appointment.html"
    form_class = AppointmentForm
    success_url = reverse_lazy("manage-appointments")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pet_sitters"] = PetSitter.objects.all()
        context["user"] = CustomUser.objects.filter(id=self.request.user.id)
        print(context["user"])
        return context

    def form_valid(self, form):
        # Set the user of the appointment based on the logged-in user
        form.instance.user = self.request.user
        return super().form_valid(form)

    def post(self, request):
        fname = request.POST.get("fname")
        lname = request.POST.get("fname")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        pet_name = request.POST.get("pet_name")
        message = request.POST.get("request")
        appointment_date = request.POST.get("appointment_date")
        petowner = PetOwner.objects.filter(user=self.request.user).first()
        appointment = Appointment.objects.create(
            user = petowner,
            first_name=fname,
            last_name=lname,
            email=email,
            phone=mobile,
            appointment_date=appointment_date,
            request=message,
            pet_name=pet_name,
            sitter=PetSitter.objects.get(id=request.POST.get('selected_pet_sitter')),
        )

        appointment.save()

        messages.add_message(request, messages.SUCCESS, f"Thanks {fname} for making an appointment, we will email you ASAP!")
        return HttpResponseRedirect(request.path)

class ManageAppointmentTemplateView(LoginRequiredMixin,ListView):
    template_name = "manage-appointments.html"
    model = Appointment
    context_object_name = "appointments"
    login_required = True
    login_url = '/login_url/'
    paginate_by = 3

    def get_queryset(self):
        # Filter appointments based on the logged-in user
        if self.request.user.user_type == CustomUser.UserType.petowner:
            return Appointment.objects.filter(user=PetOwner.objects.filter(user=self.request.user).first(),
                                              cancelled=False)
        elif self.request.user.user_type == CustomUser.UserType.petsitter:
            return Appointment.objects.filter(sitter=PetSitter.objects.filter(user=self.request.user).first(),
                                              cancelled=False)


    def post(self, request):

        date = request.POST.get("date")
        appointment_id = request.POST.get("appointment-id")
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.accepted = True
        appointment.accepted_date = datetime.datetime.now()
        appointment.save()

        data = {
            "fname":appointment.first_name,
            "date":date,
        }

        message = get_template('email.html').render(data)
        email = EmailMessage(
            "About your appointment",
            message,
            "amardeepakgautam@gmail.com",
            [appointment.email],
        )
        email.content_subtype = "html"
        email.send()

        messages.add_message(request, messages.SUCCESS, f"You accepted the appointment of {appointment.first_name}")
        return HttpResponseRedirect(request.path)


    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["pet_sitters"] = PetSitter.objects.all()
        context["appointments"] = self.get_queryset()

        # appointments = Appointment.objects.filter(user=11)
        context.update({
            "title":"Manage Appointments"
        })
        return context


class CancelAppointmentView(View):
    template_name = "manage-appointments.html"
    model = Appointment
    context_object_name = "appointments"
    login_required = True
    login_url = '/login_url/'
    paginate_by = 3

    def get_queryset(self):
        # Filter appointments based on the logged-in user
        if self.request.user.user_type == CustomUser.UserType.petowner:
            return Appointment.objects.filter(user=PetOwner.objects.filter(user=self.request.user).first(),
                                              cancelled=False)
        elif self.request.user.user_type == CustomUser.UserType.petsitter:
            return Appointment.objects.filter(sitter=PetSitter.objects.filter(user=self.request.user).first(),
                                              cancelled=False)
    def get(self,request, *args, **kwargs):
        # return HttpResponseRedirect(request.path)
        return redirect(reverse("manage-appointments"))
        pass
    def post(self, request, *args, **kwargs):
        appointment_id = request.POST.get("appointment-id")
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.cancelled = True;
        appointment.cancelled_date = timezone.now().date();
        appointment.save()
        messages.add_message(request, messages.SUCCESS, f"Appointment canceled successfully")
        return redirect(reverse("manage-appointments"))

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["pet_sitters"] = PetSitter.objects.all()
        context["appointments"] = self.get_queryset()

        # appointments = Appointment.objects.filter(user=11)
        context.update({
            "title":"Manage Appointments"
        })
        return context

class UpdateAppointmentView(View):
    template_name = "manage-appointments.html"
    model = Appointment
    context_object_name = "appointments"
    login_required = True
    login_url = '/login_url/'
    paginate_by = 3

    def get_queryset(self):
        # Filter appointments based on the logged-in user
        if self.request.user.user_type == CustomUser.UserType.petowner:
            return Appointment.objects.filter(user=PetOwner.objects.filter(user=self.request.user).first(),
                                              cancelled=False)
        elif self.request.user.user_type == CustomUser.UserType.petsitter:
            return Appointment.objects.filter(sitter=PetSitter.objects.filter(user=self.request.user).first(),
                                              cancelled=False)

    def get(self, request, *args, **kwargs):
        # return HttpResponseRedirect(request.path)
        return redirect(reverse("manage-appointments"))
        pass
    def post(self, request, *args, **kwargs):
        appointment_id = request.POST.get("appointment-id")
        new_date = request.POST.get("date")
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.appointment_date = new_date
        appointment.save()
        messages.add_message(request, messages.SUCCESS, f"Appointment updated successfully")
        return redirect(reverse("manage-appointments"))


    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["pet_sitters"] = PetSitter.objects.all()
        context["appointments"] = self.get_queryset()

        # appointments = Appointment.objects.filter(user=11)
        context.update({
            "title":"Manage Appointments"
        })
        return context