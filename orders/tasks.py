from django.core.mail import send_mail
from .models import Order
from celery import shared_task


@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name}. You have successfully placed an order. Your order id is {order.id}'
    send_mail(subject=subject,
              message=message,
              from_email='odmin.test@gmail.com',
              recipient_list=[order.email],
              fail_silently=False
              )
