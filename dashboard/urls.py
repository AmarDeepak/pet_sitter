from django.urls import path
from .views import HomeTemplateView, AppointmentTemplateView, ManageAppointmentTemplateView, CancelAppointmentView, UpdateAppointmentView

urlpatterns = [
    path("", HomeTemplateView.as_view(), name="home"),
    path("make-an-appointment/", AppointmentTemplateView.as_view(), name="appointment"),
    path("manage-appointments/", ManageAppointmentTemplateView.as_view(), name="manage-appointments"),
    path("cancel-appointment/", CancelAppointmentView.as_view(), name="cancel-appointment"),
    path("update-appointment/", UpdateAppointmentView.as_view(), name="update-appointment"),
]
