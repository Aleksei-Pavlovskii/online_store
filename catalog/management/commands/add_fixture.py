from os import write

from django.core.management import call_command
from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Добавление тестовых данных из фикстуры'


    def handle(self, *args, **kwargs):
        # Удаляем существующие записи
        Category.objects.all().delete()
        Product.objects.all().delete()

        call_command('loaddata', 'categories_fixture.json')
        call_command('loaddata', 'product_fixture.json')





