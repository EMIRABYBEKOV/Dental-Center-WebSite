from django.shortcuts import render
from .models import (
    Service,
    Doctor,
    Appointment
)


def index(request):
    model = Service.objects.all()
    context = {
        'first': model
    }
    return render(request, 'index.html', context)


def doctor(request):
    model = Doctor.objects.all()
    context = {
        'first': model
    }
    return render(request,'service.html', context)


def appointment(request):
    model = Appointment.objects.all()
    context = {
        'first': model
    }
    return render(request,'appointment.html', context)
