from django.core.management import BaseCommand

from authapp.models import DebiUser


class Command(BaseCommand):
    help = "Программно создаем суперпользователя"

    def handle(self, *args, **kwargs):
        if not DebiUser.objects.filter(username="django").exists():
            DebiUser.objects.create_superuser("django", "dj@mail.ru", "geekbrains")
