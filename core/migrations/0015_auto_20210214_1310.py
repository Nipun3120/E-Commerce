# Generated by Django 2.2.13 on 2021-02-14 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_whishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whishlist',
            name='item',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Item'),
        ),
    ]
