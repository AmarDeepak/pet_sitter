from django.shortcuts import render

from .forms import AppointmentForm
from .models import Appointment
from django.http.response import HttpResponseRedirect
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage, message
from django.conf import settings
from django.contrib import messages
from django.views.generic import ListView
import datetime
from django.template.loader import render_to_string, get_template
from users.models import PetOwner, PetSitter
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.template import Context
# Create your views here.

def petowner(request):
    #Need to validate the user.
    return render(request, 'dashboard.html')

def petsitter(request):
    return render(request, 'dashboard/pet_sitter_dashboard.html')


class HomeTemplateView(TemplateView):
    template_name = "dashboard.html"

    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        email = EmailMessage(
            subject= f"{name} from pet sitter family.",
            body=message,
            from_email="amardeepakgautam@gmail.com",
            to=['nirlesh504@hmail.com'],
            reply_to=[email]
        )
        email.send()
        return HttpResponse("Email sent successfully!")
class AppointmentTemplateView(TemplateView):
    template_name = "appointment.html"
    form_class = AppointmentForm
    success_url = reverse_lazy("manage-appointments")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pet_sitters"] = PetSitter.objects.all()
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
        message = request.POST.get("request")
        import pdb; pdb.set_trace()
        petowner = PetOwner.objects.filter(user=self.request.user).first()
        appointment = Appointment.objects.create(
            user = petowner,
            first_name=fname,
            last_name=lname,
            email=email,
            phone=mobile,
            request=message,
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
        return Appointment.objects.filter(user=PetOwner.objects.filter(user=self.request.user).first())


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
        import pdb
        pdb.set_trace()
        context = super().get_context_data(*args, **kwargs)
        context["pet_sitters"] = PetSitter.objects.all()

        # appointments = Appointment.objects.filter(user=11)
        context.update({
            "title":"Manage Appointments"
        })
        return context