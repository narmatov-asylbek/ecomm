from celery import task
from .models import Order
from django.core.mail import send_mail


@task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Добрый день, {order.first_name}. Заказ успешно оформлен'
    message = f'ID вашего заказа {order.id}'
    mail_sent = send_mail(subject, message, 'pochemuno@gmail.com', [order.email])

    return mail_sent
