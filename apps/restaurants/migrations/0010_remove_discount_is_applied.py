# Generated by Django 3.2.8 on 2021-10-11 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0009_discount_is_applied'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discount',
            name='is_applied',
        ),
    ]
