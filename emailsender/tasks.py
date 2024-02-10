from celery import shared_task
from .models import Subscriber, Quote
from .email_utils import send_email

@shared_task
def send_scheduled_email(email, subject, message):
    send_email(email, subject, message)


@shared_task
def send_quote_email(subscriber_id, quote_id):
    subscriber = Subscriber.objects.get(id=subscriber_id)
    quote = Quote.objects.get(id=quote_id)
    subject = "Your Daily Quote"
    message = f"{quote.quote_text}\n\n- {quote.author}"
    send_email(subscriber.email, subject, message)