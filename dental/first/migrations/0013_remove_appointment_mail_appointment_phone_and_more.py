# Generated by Django 4.0.1 on 2022-01-16 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0012_alter_appointment_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='mail',
        ),
        migrations.AddField(
            model_name='appointment',
            name='phone',
            field=models.CharField(default=0, max_length=20, verbose_name='phone'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='doctor',
            field=models.CharField(max_length=255, verbose_name='doctor'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='service',
            field=models.CharField(max_length=255, verbose_name='service'),
        ),
    ]
