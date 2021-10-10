# Generated by Django 3.2.8 on 2021-10-10 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_cartitem_quantity'),
        ('orders', '0005_alter_order_restaurant'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='courier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='courier_orders', to='users.profile'),
        ),
    ]
