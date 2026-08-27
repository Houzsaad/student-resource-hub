import os

from django.core.management.base import BaseCommand
from accounts.models import User


class Command(BaseCommand):
    help = "Create a superuser from environment variables"

    def handle(self, *args, **options):
        email = os.environ.get("ADMIN_EMAIL")
        password = os.environ.get("ADMIN_PASSWORD")
        full_name = os.environ.get("ADMIN_FULL_NAME")

        if not email or not password or not full_name:
            self.stdout.write(
                self.style.WARNING(
                    "Admin environment variables are not configured. Skipping."
                )
            )
            return

        email = email.lower().strip()

        # Don't create another admin if this email already exists
        if User.objects.filter(email=email).exists():
            self.stdout.write(
                self.style.SUCCESS(
                    f"Admin with email {email} already exists. Skipping."
                )
            )
            return

        User.objects.create_superuser(
            email=email,
            password=password,
            full_name=full_name,
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Superuser {email} created successfully."
            )
        )