import random
from .models import Subscriber, Quote

def get_random_subscriber():
    subscribers = list(Subscriber.objects.all())
    return random.choice(subscribers) if subscribers else None


def get_random_quote():
    quotes = list(Quote.objects.all())
    return random.choice(quotes) if quotes else None