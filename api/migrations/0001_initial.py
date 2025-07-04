# Generated by Django 4.2.23 on 2025-07-03 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.CharField(blank=True, max_length=20, unique=True)),
                ('name', models.CharField(max_length=200, verbose_name='Nombre Completo')),
                ('dob', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('contact', models.EmailField(max_length=100, verbose_name='Email de Contacto')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
