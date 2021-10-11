from django.core.mail import send_mail

from conf.settings.email_conf import EMAIL_FROM


def send_email_about_delivered_order(order):
    subject = f'Your order # {order.id} was delivered'
    message = f'Your order # {order.id} was delivered. You can report courier within 5 minutes from now. ' \
              f'Click link to report courier <a href="http://127.0.0.1:8000/api/v1/report/29/">Link</a>'
    to = order.profile.user.email

    send_mail(subject, message, EMAIL_FROM, [to])


def send_email_to_restaurant_about_order_changes(order, _type):
    to = order.restaurant.email
    if _type == 'new':
        subject = f'New Order #{order.id}'
        message = f'New Order #. link to all orders <a href="http://127.0.0.1:8000/api/v1/orders/'
    else:
        subject = f'Order # status changed'
        message = f'Order # status changed to {order.status}'

    send_mail(subject, message, EMAIL_FROM, [to])
