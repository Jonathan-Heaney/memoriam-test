from django.contrib import admin

# Register your models here.
from .models import Subscriber, Quote, QuotesSent, SubscriptionYear

admin.site.register(Subscriber)
admin.site.register(Quote)
admin.site.register(QuotesSent)
admin.site.register(SubscriptionYear)
