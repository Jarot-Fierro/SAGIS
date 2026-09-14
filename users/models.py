from django.contrib.auth.models import AbstractUser
from django.db import models

from config import settings
from core.standard.models import StandardModelEstablishment


class User(AbstractUser):
    username = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Nombre de Usuario')
    password = models.CharField(
        max_length=128,
        verbose_name='Contraseña'
    )
    role = models.ForeignKey(
        'users.Role',
        on_delete=models.CASCADE,
        verbose_name='Rol',
        related_name='user_role',
        null=True,
        blank=True,
    )
    establishment = models.ForeignKey(
        'organization.Establishment',
        on_delete=models.CASCADE,
        verbose_name='Establecimiento',
        related_name='user_establishment',
        null=True,
        blank=True,
    )
    employee = models.ForeignKey(
        'organization.Employee',
        on_delete=models.CASCADE,
        verbose_name='Funcionario',
        related_name='user_employee',
        null=True,
        blank=True,
    )
    avatar = models.ForeignKey(
        'users.Avatar',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Avatar',
        related_name='avatar_users'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha Creación',
        null=True,
        blank=True
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Última Actualización',
        null=True,
        blank=True
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(app_label)s_%(class)s_created",
        verbose_name='Creado Por'
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(app_label)s_%(class)s_updated",
        verbose_name='Actualizado Por'
    )

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['username']


class Role(StandardModelEstablishment):
    PERMISION_CHOICES = [
        (0, 'Sin Acceso'),
        (1, 'Solo Ver'),
        (2, 'Crear y Modificar'),
        (3, 'Administrador')
    ]

    name = models.CharField(
        max_length=200,
        verbose_name='Nombre del Rol')
    customers = models.IntegerField(
        choices=PERMISION_CHOICES,
        default=0,
        verbose_name='Clientes'
    )
    suppliers = models.IntegerField(
        choices=PERMISION_CHOICES,
        default=0,
        verbose_name='Proveedores'
    )
    products = models.IntegerField(
        choices=PERMISION_CHOICES,
        default=0,
        verbose_name='Productos'
    )
    purchases = models.IntegerField(
        choices=PERMISION_CHOICES,
        default=0,
        verbose_name='Compras'
    )
    sales = models.IntegerField(
        choices=PERMISION_CHOICES,
        default=0,
        verbose_name='Ventas'
    )
    inventory = models.IntegerField(
        choices=PERMISION_CHOICES,
        default=0,
        verbose_name='Inventario'
    )
    accounting = models.IntegerField(
        choices=PERMISION_CHOICES,
        default=0,
        verbose_name='Contabilidad'
    )
    reporting = models.IntegerField(
        choices=PERMISION_CHOICES,
        default=0,
        verbose_name='Reportes'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
        ordering = ['name']
        unique_together = ['name', 'establishment']


class Avatar(StandardModelEstablishment):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Nombre'
    )

    image = models.ImageField(
        upload_to='avatars/',
        verbose_name='Imagen'
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name='Activo'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Avatar'
        verbose_name_plural = 'Avatares'
        ordering = ['name']
