# Generated by Django 3.2.8 on 2021-10-09 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_address'),
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.restaurant')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
            options={
                'db_table': 'employees',
            },
        ),
    ]