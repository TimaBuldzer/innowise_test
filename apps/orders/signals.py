from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.orders.models import Order
from apps.services.email_services import send_email_to_restaurant_about_order_changes


@receiver(post_save, sender=Order)
def order_signal(sender, instance, created, **kwargs):
    if created:
        send_email_to_restaurant_about_order_changes(instance, 'new')
    else:
        send_email_to_restaurant_about_order_changes(instance, 'status_changed')
