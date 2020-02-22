# Generated by Django 3.0.3 on 2020-02-17 18:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('second_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=255)),
                ('nic_number', models.CharField(max_length=12)),
                ('mobile_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(max_length=254)),
                ('nationality', django_countries.fields.CountryField(max_length=2)),
                ('date_of_birth', models.DateField()),
                ('sex', models.CharField(max_length=6)),
                ('emergency_contact', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('designation', models.CharField(blank=True, max_length=100)),
                ('department', models.CharField(blank=True, max_length=100)),
                ('epf_etf_number', models.CharField(blank=True, max_length=10)),
                ('date', models.DateField(blank=True, max_length=500)),
                ('photo', models.ImageField(upload_to=None)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
