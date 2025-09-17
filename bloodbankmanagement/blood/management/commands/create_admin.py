from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create admin user'

    def handle(self, *args, **options):
        username = 'admin'
        email = 'admin@bloodbank.com'
        password = 'bloodbank123'  # Change this to a secure password
        
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            self.stdout.write(
                self.style.SUCCESS(f'Admin user "{username}" created successfully')
            )
            self.stdout.write(f'Email: {email}')
            self.stdout.write(f'Password: {password}')
        else:
            self.stdout.write(
                self.style.WARNING(f'Admin user "{username}" already exists')
            )
