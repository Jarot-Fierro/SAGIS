from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core.standard.admin import StandardAdmin
from users.models import User, Role, Avatar


@admin.register(User)
class UserAdmin(BaseUserAdmin, StandardAdmin):
    reset_password_value = '$$$2026_2027'

    list_display = ('username', 'email', 'first_name', 'last_name', 'establishment', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'establishment',)
    search_fields = ('username', 'email', 'first_name', 'last_name', 'establishment__name')
    autocomplete_fields = ('employee',)

    actions = ['reset_password']

    def reset_password(self, request, queryset):
        for user in queryset:
            user.set_password(self.reset_password_value)
            user.save()
        self.message_user(request, f"Se ha reseteado la contraseña de {queryset.count()} usuarios correctamente.")

    reset_password.short_description = "Resetear contraseña"

    fieldsets = (
        (None, {'fields': ('username', 'password')}),

        ('Información Personal', {
            'fields': (
                'first_name',
                'last_name',
                'email',
                'establishment',
                'role',
                'employee',
                'avatar',
            )
        }),

        ('Permisos', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),

        ('Fechas importantes', {
            'fields': (
                'last_login',
                'date_joined',
                'created_at',
                'updated_at',
                'created_by',
                'updated_by',
            )
        }),
    )


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'customers',
        'suppliers',
        'products',
        'purchases',
        'sales',
        'inventory',
        'accounting',
        'reporting'
    )


@admin.register(Avatar)
class AvatarAdmin(StandardAdmin):
    list_display = (
        'id',
        'name',
        'image',
        'is_active',
        'created_at',
        'updated_at',
        'created_by',
    )

    search_fields = (
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
