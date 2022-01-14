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
    service = models.ForeignKey(Service, verbose_name="service", on_delete=models.CASCADE, blank=True, null=True)
    doctor = models.ForeignKey(Doctor, verbose_name="doctor", on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(verbose_name="name", max_length=255)
    mail = models.EmailField(verbose_name="mail")
    date = models.CharField(verbose_name="date", max_length=255)
    time = models.CharField(verbose_name="time", max_length=255)
    acceptance = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.date
