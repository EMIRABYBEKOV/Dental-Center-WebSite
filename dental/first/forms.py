from django import forms
from .models import Appointment, Service, Doctor

# class AppointmentForm(forms.ModelForm):
#
#     name = forms.CharField(label='name', widget=forms.TextInput(attrs={'class': 'form-control'}))
#     mail = forms.EmailField(label='mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
#     service = forms.CharField(label='service', widget=forms.TextInput(attrs={'class': 'form-control'}))
#     doctor = forms.CharField(label='doctor', widget=forms.TextInput(attrs={'class': 'form-control'}))
#     date = forms.CharField(label='date', widget=forms.TextInput(attrs={'class': 'form-control'}))
#     time = forms.CharField(label='time', widget=forms.TextInput(attrs={'class': 'form-control'}))
#
#
#
#     class Meta:
#         model = Appointment
#         fields = (
#             'name', 'mail', 'service', 'doctor', 'date', 'time',
#         )
