# Generated by Django 2.2.13 on 2021-02-17 18:05

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_order_billing_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingaddress',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]