# Generated by Django 2.2.13 on 2021-02-14 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20210214_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='wishlist',
        ),
    ]
