from django.shortcuts import render, redirect
from .models import Appointment, Service, Doctor
from django.http import HttpResponseRedirect


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

def appointment(request):
    if request.method == 'POST':
        # service = Service.objects.all()
        # doctor = Doctor.objects.all()
        name = request.POST['name']
        mail = request.POST['mail']
        date = request.POST['date']
        time = request.POST['time']
        add = Appointment(name=name, mail=mail, date=date, time=time)
        add.save()
        # service.save()
        # doctor.save()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')




# def home(request):
#     service = Service.objects.all()
#     doctor = Doctor.objects.all()
#     service2 = Service.objects.all()[0:2]
#     service3 = Service.objects.all()[2:4]
#     contex = {
#         'service': service,
#         'doctor': doctor,
#         'service2': service2,
#         'service3': service3,
#     }
#     return render(request, 'index.html', contex)


# @require_POST
# def add(request):
#     form = AppointmentForm(request.POST)
#     if form.is_valid():
#         new_app = Appointment(name=request.POST['service'])
#         new_app = Appointment(name=request.POST['doctor'])
#         new_app = Appointment(name=request.POST['name'])
#         new_app = Appointment(name=request.POST['mail'])
#         new_app = Appointment(name=request.POST['date'])
#         new_app = Appointment(name=request.POST['time'])
#         new_app.save()
#     return redirect('home')
