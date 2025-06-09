from os.path import join
from django.conf import settings
from django.core.files.images import ImageFile
from django.core.management.base import BaseCommand
from event_feed.models import User, Achievement, Note, Advertisement


class Command(BaseCommand):
    help = "Seed the database with sample users and achievements"

    def handle(self, *args, **kwargs):
        # Create users --------------------------------------------------------
        User.objects.create_superuser(
            username="admin", password="admin"
        )
        User.objects.create_user(
            username="vasya", first_name="Vasya", last_name="Petrov"
        )
        User.objects.create_user(
            username="petya", first_name="Petya", last_name="Ivanov"
        )

        # Create achievement --------------------------------------------------
        icons_path = join(settings.BASE_DIR, 'icon_templates')

        golden_icon_name = "gold-medal.png"
        with open(join(icons_path, golden_icon_name), "rb") as f:
            Achievement.objects.get_or_create(
                title="Received a Gold medal",
                condition="For receiving 1000 experience points in the app",
                icon=ImageFile(f, name=golden_icon_name)
            )

        silver_icon_name = "silver-medal.png"
        with open(join(icons_path, silver_icon_name), "rb") as f:
            Achievement.objects.get_or_create(
                title="Received a Silver medal",
                condition="For receiving 700 experience points in the app",
                icon=ImageFile(f, name=silver_icon_name)
            )

        # Create notes --------------------------------------------------------
        Note.objects.create(
            title="Completed Mission",
            body="Completed a secret mission",
            created_by=User.objects.get(username='vasya')
        )
        # Create Advertisements -----------------------------------------------
        silver_icon_name = "silver-medal.png"
        with open(join(icons_path, silver_icon_name), "rb") as f:
            Advertisement.objects.create(
                title="The console is for sale",
                description="Selling PS4 console in excellent condition",
                image=ImageFile(f, name=silver_icon_name),
                url="https://www.google.com/"
            )
        self.stdout.write(self.style.SUCCESS("Seed data created."))
