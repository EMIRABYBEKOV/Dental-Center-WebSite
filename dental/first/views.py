from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Appointment, Service, Doctor
from .forms import AppointmentForm
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse

def home(request):
    service = Service.objects.all()
    doctor = Doctor.objects.all()
    service2 = Service.objects.all()[0:2]
    service3 = Service.objects.all()[2:4]
    contex = {
        'service': service,
        'doctor': doctor,
        'service2': service2,
        'service3': service3

    }
    return render(request, 'index.html', contex)

class MakeApointmentView(View):
    def post(self, request, *args, **kwargs):
        form = AppointmentForm()
        if form.is_valid():
            new_app = form.save(commit=False)
            new_app.name = form.cleaned_data['name']
            new_app.mail = form.cleaned_data['mail']
            new_app.service = form.cleaned_data['service']
            new_app.doctor = form.cleaned_data['doctor']
            new_app.date = form.cleaned_data['date']
            new_app.time = form.cleaned_data['time']
            new_app.save()
            messages.add_message(request, messages.INFO, 'Спасибо! Подходите по указанной дате и времени')
            return HttpResponseRedirect('/')
        return HttpResponseRedirect(request, 'index.html', {'form':form})


