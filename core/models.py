from django.db import models

from core.standard.models import StandardModel, StandardModelEstablishment


class Unit(StandardModel):
    name = models.CharField(
        unique=True,
        max_length=200,
        verbose_name='Nombre'
    )
    symbol = models.CharField(
        unique=True,
        max_length=200,
        verbose_name='Simbolo'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Unidad'
        verbose_name_plural = 'Unidades'
        ordering = ['name']


class Country(StandardModel):
    name = models.CharField(
        max_length=60,
        verbose_name="País"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Países"
        ordering = ['name']


class Currency(StandardModel):
    name = models.CharField(
        max_length=60,
        verbose_name="País"
    )
    symbol = models.CharField(
        max_length=20,
        verbose_name="Simbolo"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Moneda"
        verbose_name_plural = "Monedas"
        ordering = ['name']
