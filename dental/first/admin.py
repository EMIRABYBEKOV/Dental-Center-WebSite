from django.contrib import admin
from .models import Doctor, Service, Appointment

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'time',)
    list_filter = ('name', 'price', 'doctor',)
    search_fields = ('name', 'description',)
    raw_id_fields = ('doctor',)
    ordering = ('name', 'price',)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'profession',)
    list_filter = ('profession', 'service',)
    search_fields = ('name', 'profession', 'service',)
    ordering = ('profession', 'service',)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('service', 'doctor', 'date', 'time', 'acceptance',)
    list_filter = ('service', 'doctor', 'date', 'time', 'acceptance',)
    search_fields = ('service', 'doctor', 'date', 'time', 'acceptance',)
    ordering = ('service', 'doctor', 'date', 'time', 'acceptance',)

