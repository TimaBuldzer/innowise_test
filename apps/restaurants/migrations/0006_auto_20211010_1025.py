# Generated by Django 3.2.8 on 2021-10-10 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_dish_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='restaurants/dishes/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='dish',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]