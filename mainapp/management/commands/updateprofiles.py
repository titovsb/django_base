from django.core.management.base import BaseCommand
from authapp.models import DebiUser, DebiUserProfile
from mainapp.utils import get_or_create


class Command(BaseCommand):
    help = "create|update user profiles"

    def handle(self, *args, **kwargs):
        users = DebiUser.objects.all()
        for user in users:
            get_or_create(DebiUserProfile, *args, **kwargs)
