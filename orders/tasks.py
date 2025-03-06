from celery import shared_task
from django.core.mail import send_mail
from .models import Order

@shared_task
def order_created(order_id):
    """
    مهمة لإرسال بريد إلكتروني تأكيدي عند إنشاء الطلب بنجاح.
    """
    order = Order.objects.get(id=order_id)  # جلب الطلب من قاعدة البيانات
    subject = f'Order nr. {order.id}'  # عنوان البريد الإلكتروني
    message = f'Dear {order.first_name},\n\n' \
              f'You have successfully placed an order.\n' \
              f'Your order ID is {order.id}.'
    
    # إرسال البريد الإلكتروني
    mail_sent = send_mail(
        subject,
        message,
        'admin@myshop.com',  # البريد الإلكتروني للمرسل
        [order.email]  # البريد الإلكتروني للمستلم
    )
    
    return mail_sent  # إرجاع نتيجة الإرسال (نجح أو فشل)
