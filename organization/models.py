from django.db import models

from core.standard.models import StandardModel, StandardModelEstablishment


class Establishment(StandardModel):
    name = models.CharField(
        max_length=200,
        verbose_name='Nombre'
    )

    run = models.CharField(
        max_length=20,
        unique=True,
        verbose_name='RUN'
    )

    alias = models.CharField(
        max_length=20,
        unique=True,
        null=True,
        blank=True,
        verbose_name='Alias'
    )

    area = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Área'
    )

    address = models.TextField(
        blank=True,
        null=True,
        verbose_name='Dirección'
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Teléfono'
    )

    anexo = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Anexo'
    )

    email = models.EmailField(
        blank=True,
        null=True,
        verbose_name='Correo'
    )

    logo = models.ImageField(
        upload_to='establecimientos/logos/%Y',
        blank=True,
        null=True,
        verbose_name='Logo'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Establecimiento'
        verbose_name_plural = 'Establecimientos'


class Department(StandardModelEstablishment):
    name = models.CharField(
        max_length=200,
        verbose_name='Nombre'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Departamento/Servicio'
        verbose_name_plural = 'Departamentos/Servicios'
        ordering = ['name']


class Employee(StandardModel):
    names = models.CharField(
        max_length=200,
        verbose_name='Nombre'
    )
    rut = models.CharField(
        max_length=20,
        unique=True,
        verbose_name='RUN'
    )
    email = models.EmailField(
        blank=True,
        null=True,
        verbose_name='Correo'
    )
    anexo = models.CharField(
        max_length=20,
    )
    phone = models.CharField(
        max_length=20
    )
    department = models.ForeignKey(
        'organization.Department',
        on_delete=models.CASCADE,
        verbose_name='Departamento/Servicio',
        related_name='leader_departament'
    )

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'
        ordering = ['names']


class DepartmentLeadership(StandardModel):
    ROLE = [
        ('JEFE TITULAR', 'JEFE TITULAR'),
        ('JEFE SUBROGANTE', 'JEFE SUBROGANTE'),
        ('SUBROGANTE', 'SUBROGANTE'),

    ]

    employee = models.ForeignKey(
        'organization.Employee',
        on_delete=models.PROTECT,
        related_name='leaderships',
        verbose_name='Funcionario'
    )

    department = models.ForeignKey(
        'organization.Department',
        on_delete=models.PROTECT,
        related_name='leaderships',
        verbose_name='Departamento/Servicio'
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE,
        verbose_name='Tipo de jefatura'
    )

    start_date = models.DateField(
        verbose_name='Fecha de inicio'
    )

    end_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Fecha de término'
    )

    def __str__(self):
        return f'{self.employee} - {self.get_role_display()}'

    class Meta:
        verbose_name = 'Jefatura'
        verbose_name_plural = 'Jefaturas'
        ordering = ['employee']
