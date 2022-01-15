from django.urls import path
from .import views

urlpatterns = [
    path('home/', views.home,  name='home'),
    path('/', views.appointment,  name='appointment'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('price/', views.price, name='price'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact')
]

