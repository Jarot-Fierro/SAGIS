from django.contrib import admin

from core.models import Communes
from core.standard.admin import StandardAdmin


@admin.register(Communes)
class CommunesAdmin(StandardAdmin):
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
