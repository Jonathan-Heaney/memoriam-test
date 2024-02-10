from django.shortcuts import render
from django.http import HttpResponse
from .email_utils import send_email
from .tasks import send_scheduled_email
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