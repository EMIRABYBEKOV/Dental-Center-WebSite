from django.db import models

class Service(models.Model):
    name = models.CharField(verbose_name="service_name", max_length=255)
    price = models.PositiveIntegerField(default=0)
    description = models.CharField(verbose_name="description")
    doctor = models.ForeignKey('Doctor', verbose_name="doctor", on_delete=models.CASCADE)
    img = models.ImageField(verbose_name='Image')
    time = models.CharField(verbose_name="time", default="24/7")

class Doctor(models.Model):
    name = models.CharField(verbose_name="name", max_length=255)
    profession = models.CharField(verbose_name="profession", max_length=255)
    img = models.ImageField(verbose_name="image")
    service = models.ManyToManyField(Service, verbose_name="service", on_delete=models.CASCADE)

class Appointment(models.Model):
    service = models.ForeignKey(Service, verbose_name="service", on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, verbose_name="doctor", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="name", max_length=255)
    email = models.EmailField(verbose_name="mail")
    date = models.CharField(verbose_name="date", max_length=255)
    time = models.CharField(verbose_name="time", max_length=255)
    acceptance = models.BooleanField(default=False)

