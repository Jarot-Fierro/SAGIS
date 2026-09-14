# Guía de Uso: Administración Estándar (`StandardAdmin`)

Esta guía explica cómo utilizar la clase base `StandardAdmin` definida en `core/standard/admin.py` para unificar el
comportamiento del panel administrativo de Django.

## Características de `StandardAdmin`

Al heredar de `StandardAdmin`, tu modelo obtendrá automáticamente:

1. **Import/Export:** Integración con `django-import-export` para cargar y descargar datos.
2. **Historial de Cambios:** Registro de auditoría mediante `django-simple-history`.
3. **Auditoría Automática:** Los campos `created_by` y `updated_by` se llenan automáticamente con el usuario que realiza
   la acción.
4. **Gestión de Actividad:**
    - Columna visual para el estado `is_active`.
    - Acciones masivas para "Activar registros seleccionados" y "Desactivar registros seleccionados".
5. **Campos de Solo Lectura:** Los campos `created_by`, `updated_by`, `created_at` y `updated_at` se configuran
   automáticamente como solo lectura.

---

## Ejemplo de uso

Para aplicar esta configuración a un modelo, simplemente hereda de `StandardAdmin` al registrarlo en el archivo
`admin.py` de tu aplicación.

```python
from django.contrib import admin
from core.standard.admin import StandardAdmin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(StandardAdmin):
    # Puedes añadir tus configuraciones adicionales de Django Admin
    list_display = ('nombre', 'codigo', 'precio')
    search_fields = ('nombre', 'codigo')
    list_filter = ('categoria',)
    
    # Nota: 'active_status' se añade automáticamente al final de list_display
    # mediante el método get_list_display de StandardAdmin.
```

## Consideraciones Técnicas

### 1. Auditoría en `save_model`

`StandardAdmin` sobrescribe `save_model` para asegurar que el usuario actual quede registrado:

- Si es una creación, se asigna `created_by`.
- En cada guardado, se actualiza `updated_by`.

### 2. Acciones Personalizadas

Las acciones `activate_records` y `deactivate_records` realizan un `.update(is_active=...)` sobre el queryset
seleccionado, lo que es eficiente para cambios masivos.

### 3. Requisitos del Modelo

Para aprovechar todas las funcionalidades, se recomienda que el modelo cuente con los siguientes campos (aunque no son
obligatorios para que el admin cargue, las funciones de auditoría y estado los buscarán):

- `is_active` (BooleanField)
- `created_by` (ForeignKey a User)
- `updated_by` (ForeignKey a User)
- `created_at` (DateTimeField)
- `updated_at` (DateTimeField)
