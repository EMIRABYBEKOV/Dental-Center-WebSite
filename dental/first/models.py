from django.db import models


class Service(models.Model):
    name = models.CharField(verbose_name="service_name", max_length=255)
    price = models.PositiveIntegerField(default=0)
    description1 = models.CharField(verbose_name="description", max_length=25)
    description2 = models.CharField(verbose_name="description", max_length=25)
    description3 = models.CharField(verbose_name="description", max_length=25)
    doctor = models.ManyToManyField('Doctor', verbose_name="doctor", related_name="doctor")
    img = models.ImageField(verbose_name='Image', blank=True)
    time = models.CharField(verbose_name="time", default="24/7", max_length=20)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(verbose_name="name", max_length=255)
    profession = models.CharField(verbose_name="profession", max_length=255)
    img = models.ImageField(verbose_name="image", blank=True)
    service = models.ManyToManyField(Service, verbose_name="service", related_name="service", blank=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):

    service = models.CharField(verbose_name="service",max_length=255)
    doctor = models.CharField(verbose_name="doctor",max_length=255)
    name = models.CharField(verbose_name="name", max_length=255)
    phone = models.CharField(verbose_name="phone", max_length=20)
    date = models.CharField(verbose_name="date", max_length=255)
    time = models.CharField(verbose_name="time", max_length=255)
    acceptance = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.date


class Review(models.Model):
    name = models.CharField(max_length=20, verbose_name='name')
    comment = models.TextField(verbose_name='comment')
    img = models.ImageField(verbose_name='img')

    def __str__(self):
        return self.name
