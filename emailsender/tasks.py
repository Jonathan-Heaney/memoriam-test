from celery import shared_task
from .email_utils import send_email

@shared_task
def send_scheduled_email(email, subject, message):
    send_email(email, subject, message)