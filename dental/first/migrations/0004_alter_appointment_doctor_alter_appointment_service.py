# Generated by Django 4.0.1 on 2022-01-13 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0003_rename_email_appointment_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='first.doctor', verbose_name='doctor'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='first.service', verbose_name='service'),
        ),
    ]
