from django.shortcuts import render
from django.http import HttpResponse
from .email_utils import send_email
from .utils import get_random_quote, get_random_subscriber
from .tasks import send_scheduled_email, send_quote_email
from datetime import datetime, timedelta
import random

# Create your views here.
def test_email(request):
    subject = "Test Email"
    to_email = "jonathan.heaney@gmail.com"
    body = "This is a test email from Django using AWS SES."
    send_email(to_email, subject, body)
    return HttpResponse("Test email sent.")


def schedule_emails(request):
    subscriber_email = 'jonathan.heaney@gmail.com'
    random_minutes = random.randint(1, 4)
    scheduled_time = datetime.now() + timedelta(minutes=random_minutes)

    send_scheduled_email.apply_async(('jonathan.heaney@gmail.com', 'Hi from Celery', 'Celery is working!'), eta=scheduled_time)

    return HttpResponse("Email scheduled.")


def send_test_email(request):
   subscriber = get_random_subscriber()
   quote = get_random_quote()
   if subscriber and quote:
       send_quote_email(subscriber.id, quote.id)
       return HttpResponse("Test quote email sent.")
   return HttpResponse("No subscriber or quote found.")