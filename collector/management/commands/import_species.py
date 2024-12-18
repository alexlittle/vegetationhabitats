import csv
from django.core.management.base import BaseCommand
from collector.models import Species


class Command(BaseCommand):
    help = 'Imports species data from a CSV file into the database'

    def handle(self, *args, **kwargs):
        # Path to CSV file
        csv_file_path = '/path/to/species.csv'  # Replace with actual path

        try:
            with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:
                    scientific_name = row.get('scientificName')
                    Species.objects.update_or_create(
                        name=scientific_name,
                    )
                    print(f"Added: {scientific_name}")

            self.stdout.write(self.style.SUCCESS('Successfully imported species data'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {e}"))
