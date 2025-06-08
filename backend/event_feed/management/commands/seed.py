from os.path import join
from django.conf import settings
from django.core.files.images import ImageFile
from django.core.management.base import BaseCommand
from event_feed.models import User, Achievement


class Command(BaseCommand):
    help = "Seed the database with sample users and achievements"

    def handle(self, *args, **kwargs):
        User.objects.create_superuser(
            username="admin", password="admin"
        )
        User.objects.create_user(
            username="vasya", first_name="Vasya", last_name="Petrov"
        )
        User.objects.create_user(
            username="petya", first_name="Petya", last_name="Ivanov"
        )

        icons_path = join(settings.BASE_DIR, 'icon_templates')

        golden_icon_name = "gold-medal.png"
        with open(join(icons_path, golden_icon_name), "rb") as f:
            image = ImageFile(f, name=golden_icon_name)
            Achievement.objects.get_or_create(
                name="Received a Gold medal",
                condition="For receiving 1000 experience points in the app",
                icon=image
            )

        silver_icon_name = "silver-medal.png"
        with open(join(icons_path, silver_icon_name), "rb") as f:
            image = ImageFile(f, name=silver_icon_name)
            Achievement.objects.get_or_create(
                name="Received a Silver medal",
                condition="For receiving 700 experience points in the app",
                icon=image
            )

        self.stdout.write(self.style.SUCCESS("Seed data created."))
