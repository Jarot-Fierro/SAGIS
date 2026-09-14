from django.contrib import admin

from core.standard.admin import StandardAdmin
from organization.models import Establishment, Department, Employee, DepartmentLeadership


@admin.register(Establishment)
class EstablishmentAdmin(StandardAdmin):
    list_display = (
        'id',
        'name',
        'run',
        'alias',
        'address',
        'email',
        'logo',
        'created_at',
        'updated_at',
        'created_by',
    )

    search_fields = (
        'id',
        'name',
        'run',
        'alias',
        'address',
        'email'
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


@admin.register(Department)
class DepartmentAdmin(StandardAdmin):
    list_display = (
        'id',
        'name',
        'establishment',
        'created_at',
        'updated_at',
        'created_by',
    )

    search_fields = (
        'id',
        'name',
        'establishment__name',
    )

    list_filter = (
        'establishment',
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


@admin.register(Employee)
class EmployeeAdmin(StandardAdmin):
    list_display = (
        'id',
        'names',
        'rut',
        'email',
        'department',
        'created_at',
    )

    search_fields = (
        'id',
        'names',
        'rut',
        'email',
        'phone',
        'anexo',
        'department__name',
    )

    list_filter = (
        'department',
        'is_active',
        'created_at',
        'updated_at',
    )
    autocomplete_fields = ('department',)
    list_display_links = (
        'names',
    )

    ordering = (
        'names',
    )


@admin.register(DepartmentLeadership)
class DepartmentLeadershipAdmin(StandardAdmin):
    list_display = (
        'id',
        'employee',
        'department',
        'role',
        'start_date',
        'end_date',
        'created_at',
    )

    search_fields = (
        'id',
        'employee__names',
        'department__name',
        'role',
    )

    list_filter = (
        'role',
        'department',
        'is_active',
        'created_at',
        'updated_at',
    )
    autocomplete_fields = ('employee', 'department',)

    list_display_links = (
        'employee',
    )

    ordering = (
        '-start_date',
    )
