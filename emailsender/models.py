from django.db import models

# Create your models here.
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    subscription_date = models.DateField(auto_now_add=True)
    emails_sent_count = models.IntegerField(default=0)

    def __str__(self):
        return self.email


class Quote(models.Model):
    quote_text = models.TextField()
    author = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.quote_text[:50]}..."
    

class QuotesSent(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    sent_date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('quote', 'subscriber')


class SubscriptionYear(models.Model):
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    year_start_date = models.DateField()
    year_end_date = models.DateField()
    emails_sent_this_year = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.subscriber.email} ({self.year_start_date} - {self.year_end_date})"
