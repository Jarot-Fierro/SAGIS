from pathlib import Path

from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand

from accounting.models import AccountType
from core.management.commands.vars import *
from core.models import Unit, Country, Currency
from users.models import Avatar, User, Role


class Command(BaseCommand):
    help = 'Carga los datos iniciales del sistema'

    def handle(self, *args, **options):

        for data in UNITS:
            Unit.objects.get_or_create(
                name=data['name'],
                defaults={
                    'symbol': data['symbol']
                }
            )

        for data in COUNTRIES:
            Country.objects.get_or_create(
                name=data['name']
            )

        for data in CURRENCIES:
            Currency.objects.get_or_create(
                name=data['name'],
                defaults={
                    'symbol': data['symbol']
                }
            )
        for data in ACCOUNT_TYPE:
            AccountType.objects.get_or_create(
                name=data['name'],
            )

        avatars_path = (
                Path(settings.BASE_DIR)
                / 'core'
                / 'static'
                / 'core'
                / 'img'
        )

        for avatar_data in AVATARS:

            avatar, created = Avatar.objects.get_or_create(
                name=avatar_data['name'],
                defaults={
                    'is_active': True,
                }
            )

            if created:
                image_path = avatars_path / avatar_data['filename']

                with open(image_path, 'rb') as image_file:
                    avatar.image.save(
                        avatar_data['filename'],
                        File(image_file),
                        save=True
                    )

        for data in ROLES:
            Role.objects.get_or_create(
                name=data['name'],
                defaults={
                    'customers': data['customers'],
                    'suppliers': data['suppliers'],
                    'products': data['products'],
                    'purchases': data['purchases'],
                    'sales': data['sales'],
                    'inventory': data['inventory'],
                    'accounting': data['accounting'],
                    'reporting': data['reporting'],
                }
            )

        admin_role = Role.objects.get(
            name='ADMINISTRADOR'
        )

        root_user, created = User.objects.get_or_create(
            username='11.111.111-1',
            defaults={
                'email': 'root@root.cl',
                'first_name': 'Administrador',
                'role': admin_role,
                'is_staff': True,
                'is_superuser': True,
                'is_active': True,
            }
        )

        if created:
            root_user.set_password('root')
            root_user.save()

        self.stdout.write(
            self.style.SUCCESS(
                'Datos iniciales cargados correctamente.'
            )
        )
