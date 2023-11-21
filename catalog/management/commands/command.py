from django.core.management import BaseCommand
from catalog.models import Product, Categoties
import json


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('data.json', 'r') as file:
            data = json.load(file)

        # Удаляем все существующие продукты и категории
        Product.objects.all().delete()
        Categoties.objects.all().delete()

        categories_created = []

        # Создаем новые категории и продукты
        for category_data in data:
            # Создаем объект категории
            category = Categoties.objects.create(**category_data['fields']['name'])
            categories_created.append(category)
            print(categories_created)