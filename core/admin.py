from django.contrib import admin

from core.models import Unit, Country, Currency
from core.standard.admin import StandardAdmin


@admin.register(Unit)
class UnitAdmin(StandardAdmin):
    list_display = (
        'id',
        'name',
        'symbol',
        'is_active',
        'created_at',
        'updated_at',
        'created_by',
    )

    search_fields = (
        'id',
        'name',
        'symbol',
    )

    list_filter = (
        'is_active',
        'created_at',
        'updated_at',
    )

    list_display_links = (
        'name',
    )

    ordering = (
        'name',
    )


@admin.register(Country)
class CountryAdmin(StandardAdmin):
    list_display = (
        'id',
        'name',
        'is_active',
        'created_at',
        'updated_at',
        'created_by',
    )

    search_fields = (
        'id',
        'name',
    )

    list_filter = (
        'is_active',
        'created_at',
        'updated_at',
    )

    list_display_links = (
        'name',
    )

    ordering = (
        'name',
    )


@admin.register(Currency)
class CurrencyAdmin(StandardAdmin):
    list_display = (
        'id',
        'name',
        'is_active',
        'created_at',
        'updated_at',
        'created_by',
    )

    search_fields = (
        'id',
        'name',
    )

    list_filter = (
        'is_active',
        'created_at',
        'updated_at',
    )

    list_display_links = (
        'name',
    )

    ordering = (
        'name',
    )
