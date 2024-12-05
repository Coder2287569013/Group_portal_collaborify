from django.contrib.auth.management.commands.createsuperuser import Command as BaseCommand
from django.core.management import CommandError
from django.contrib.auth.models import Group
from getpass import getpass
from auth_sys.models import CustomUser

class Command(BaseCommand):
    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument("--first_name", required=False, help="First name")
        parser.add_argument("--last_name", required=False, help="Last name")
        parser.add_argument("--role", required=False, help="Role of the user")

    def handle(self, *args, **options):
        email = options.get('email')
        if not email:
            email = input('Email: ').strip()

        password = options.get('password') or getpass("Password: ")
        confirm_password = options.get('password') or getpass("Confirm Password: ")
        first_name = options.get('first_name') or input('First name: ').strip()
        last_name = options.get('last_name') or input('Last name: ').strip()

        try:
            group, created = Group.objects.get_or_create(name="Administrator")
            if password == confirm_password:
                user = CustomUser.objects.create_superuser(
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                    role=group  
                )

        except Exception as e:
            raise CommandError(f"Error creating superuser: {str(e)}")

        self.stdout.write(self.style.SUCCESS(f"Superuser {first_name} {last_name} created successfully!"))
