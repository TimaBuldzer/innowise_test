# Generated by Django 3.2.8 on 2021-10-11 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_auto_20211010_1025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.IntegerField(default=0)),
                ('discount_type', models.CharField(choices=[('discount', 'Discount'), ('one plus one', 'One plus one')], default='discount', max_length=25)),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.dish')),
            ],
            options={
                'db_table': 'discounts',
            },
        ),
    ]