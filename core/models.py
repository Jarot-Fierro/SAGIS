from django.db import models

from core.standard.models import StandardModel, StandardModelEstablishment


class Communes(StandardModel):
    name = models.CharField(
        unique=True,
        max_length=200,
        verbose_name='Nombre'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Comuna'
        verbose_name_plural = 'Comunas'
        ordering = ['name']
