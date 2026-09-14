from pathlib import Path

from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand

from core.management.commands.vars import *
from organization.models import Establishment
from users.models import Avatar, User, Role


class Command(BaseCommand):
    help = 'Carga los datos iniciales del sistema'

    def handle(self, *args, **options):
        for data in ESTABLISHMENTS:
            Establishment.objects.get_or_create(
                name=data['name'],
                run=data['run'],
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
                    'kardex': data['kardex'],
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
