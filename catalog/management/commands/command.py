from django.core.management import BaseCommand
from catalog.models import Product, Categoties
from django.core.management import call_command
class Command(BaseCommand):
    def handle(self, *args, **options):
        call_command('dumpdata','catalog', output='data.json')
        Product.objects.all().delete()
        Categoties.objects.all().delete()

        call_command('loaddata', '/home/geydarovr/Загрузки/two_django_djob/data.json')
