from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Создаёт группу модераторов продуктов и назначает ей права"

    def handle(self, *args, **options):
        group, _ = Group.objects.get_or_create(name="Модератор продуктов")

        permissions = Permission.objects.filter(
            content_type__app_label="catalog",
            codename__in=(
                "change_product",
                "can_unpublish_product",
            ),
        )
        group.permissions.set(permissions)

        self.stdout.write(
            self.style.SUCCESS(
                "Группа «Модератор продуктов» создана, права назначены"
            )
        )