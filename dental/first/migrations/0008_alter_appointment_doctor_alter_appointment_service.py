# Generated by Django 4.0.1 on 2022-01-14 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0007_alter_appointment_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='doctor',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='doctor'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='service',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='service'),
        ),
    ]
