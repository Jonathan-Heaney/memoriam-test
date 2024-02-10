import csv
from django.core.management.base import BaseCommand
from emailsender.models import Subscriber, Quote
from django.utils.dateparse import parse_date

class Command(BaseCommand):
    help = 'Import subscribers and quotes from CSV files'

    def add_arguments(self, parser):
        parser.add_argument('subscribers_csv', type=str, help='The CSV file with subscriber data.')
        parser.add_argument('quotes_csv', type=str, help='The CSV file with quote data.')

    def handle(self, *args, **options):
        # Import Subscribers
        with open(options['subscribers_csv'], newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Subscriber.objects.create(
                    first_name=row['first_name'],
                    last_name=row['last_name'],
                    email=row['email'],
                    subscription_date=parse_date(row['subscription_date'])
                )

        # Import Quotes
        with open(options['quotes_csv'], newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Quote.objects.create(
                    quote_text=row['quote_text'],
                    author=row['author']
                )

        self.stdout.write(self.style.SUCCESS('Successfully imported data from CSV files'))