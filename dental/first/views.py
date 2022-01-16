from django.shortcuts import render, redirect
from .models import Appointment, Service, Doctor, Review
from django.http import HttpResponseRedirect


def home(request):
    service_main = Service.objects.all()
    doctor = Doctor.objects.all()
    service2 = Service.objects.all()[0:2]
    service3 = Service.objects.all()[2:4]
    review = Review.objects.all()
    doctor2 = Doctor.objects.all()[0:2]
    doctor3 = Doctor.objects.all()[2:5]
    contex = {
        'service_main': service_main,
        'doctor': doctor,
        'service2': service2,
        'service3': service3,
        'review': review,
        'doctor2': doctor2,
        'doctor3': doctor3,
    }
    return render(request, 'index.html', contex)

def appointment(request):
    if request.method == 'POST':
        if 'service' in request.POST:
            service = request.POST['service']
        else:
            service = False
        if 'doctor' in request.POST:
            doctor = request.POST['doctor']
        else:
            doctor = False
        # service = request.POST.get['service', False]
        # doctor = Doctor.objects.all()
        name = request.POST['name']
        phone = request.POST['phone']
        date = request.POST['date']
        time = request.POST['time']
        add = Appointment(service=service, doctor=doctor, name=name, phone=phone, date=date, time=time)
        if service != 'Выбрать услугу' and doctor != 'Выбрать доктора':
            add.save()
        # service.save()
        # doctor.save()
            return HttpResponseRedirect('home/')
        else:
            return HttpResponseRedirect('home/')
    else:
        return HttpResponseRedirect('home/')


def about(request):
    contex = {}
    return render(request, 'about.html', contex)

def service(request):
    service2 = Service.objects.all()[0:2]
    service3 = Service.objects.all()[2:4]
    contex = {
        'service2': service2,
        'service3': service3,
    }
    return render(request, 'service.html', contex)

def price(request):
    service_main = Service.objects.all()
    contex = {
        'service_main': service_main,
    }
    return render(request, 'price.html', contex)

def team(request):
    doctor2 = Doctor.objects.all()[0:2]
    doctor3 = Doctor.objects.all()[2:5]
    contex = {
        'doctor2': doctor2,
        'doctor3': doctor3,
    }
    return render(request, 'team.html', contex)

def contact(request):
    contex = {}
    return render(request, 'contact.html', contex)




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
