from django.urls import path
from .models import Service, Doctor, Appointment
from .views import index

urlpatterns =[
    path('', index, name='home')
]
