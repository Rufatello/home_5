from django.core.management import BaseCommand
from users.models import User
class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='1@mail.ru',
            first_name='rufat',
            last_name='geydarov',
            is_superuser=True,
            is_staff=True,
            is_active=True

        )

        user.set_password('12345')
        user.save()